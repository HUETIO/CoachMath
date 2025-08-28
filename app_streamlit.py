import asyncio

try:
    asyncio.get_running_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

import os, time, io, uuid
from dotenv import load_dotenv
import streamlit as st
from pypdf import PdfReader

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnableParallel, RunnablePassthrough

load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")
if not API_KEY:
    st.error("Falta GOOGLE_API_KEY en .env")
    st.stop()

st.set_page_config(page_title="RAG Matemáticas (Gemini)", page_icon="🧠", layout="wide")
st.title("🧠 RAG de Matemáticas con Gemini")

# -------- Utilidades --------
def extract_text_from_pdf_bytes(pdf_bytes: bytes) -> str:
    reader = PdfReader(io.BytesIO(pdf_bytes))
    pieces = []
    for i, page in enumerate(reader.pages):
        t = page.extract_text() or ""
        if t.strip():
            pieces.append(f"[PAG {i+1}]\n{t}")
    return "\n\n".join(pieces)

def split_docs(text: str):
    splitter = RecursiveCharacterTextSplitter(chunk_size=900, chunk_overlap=150)
    return splitter.create_documents([text])

def build_vectorstore(docs):
    emb = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")
    return FAISS.from_documents(docs, emb)

def load_or_create_vs(uploaded_file):
    if "vs" in st.session_state and st.session_state["vs"] is not None:
        return st.session_state["vs"]
    # Si hay un PDF subido, usarlo; si no, usar por defecto data/matematicas.pdf
    if uploaded_file:
        text = extract_text_from_pdf_bytes(uploaded_file.getvalue())
    else:
        default_path = "data/matematicas.pdf"
        if not os.path.exists(default_path):
            st.warning("Sube un PDF o coloca data/matematicas.pdf")
            st.stop()
        with open(default_path, "rb") as f:
            text = extract_text_from_pdf_bytes(f.read())
    docs = split_docs(text)
    vs = build_vectorstore(docs)
    st.session_state["vs"] = vs
    return vs

# -------- Modelos / Prompts --------
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0.2)

RAG_TEMPLATE = """Eres un profesor de matemáticas. Responde con claridad y rigor.
Usa EXCLUSIVAMENTE el contexto si es suficiente; si no lo es, dilo.
Incluye referencias [PAG N] de donde sacaste la info.

Pregunta del usuario: {question}

Contexto:
{context}

Respuesta:"""
rag_prompt = PromptTemplate.from_template(RAG_TEMPLATE)

GUIDE_TEMPLATE = """Genera una guía educativa en Markdown sobre el concepto: "{concepto}".
Estructura:
# {concepto}
## Definición
(3-5 líneas)

## Ejemplo sencillo (paso a paso)
- Planteamiento
- Desarrollo
- Resultado

## Ejemplo avanzado (paso a paso)

## 3 ejercicios propuestos

## Soluciones

Usa el contexto del material y cita [PAG N] cuando aplique.
Contexto:
{context}
"""
guide_prompt = PromptTemplate.from_template(GUIDE_TEMPLATE)

# -------- Sidebar --------
with st.sidebar:
    st.header("⚙️ Configuración")
    uploaded_pdf = st.file_uploader("Sube tu PDF de matemáticas", type=["pdf"])
    temperature = st.slider("Creatividad (temperature)", 0.0, 1.0, 0.2, 0.05)

col1, col2 = st.columns([2,1])

with col1:
    st.subheader("Chat RAG")
    query = st.text_input("Haz una pregunta (ej: ¿qué es continuidad?)", "")
    if st.button("Buscar y responder", use_container_width=True):
        vs = load_or_create_vs(uploaded_pdf)
        retriever = vs.as_retriever(search_kwargs={"k": 4})
        chain = (
            RunnableParallel({"context": retriever | (lambda ds: "\n\n".join(d.page_content for d in ds)),
                              "question": RunnablePassthrough()})
            | rag_prompt
            | ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=temperature)
        )
        t0 = time.perf_counter()
        resp = chain.invoke(query)
        dt = time.perf_counter() - t0

        st.markdown("### Respuesta")
        st.write(resp.content)
        st.caption(f"⏱️ Latencia: {dt:.2f}s")

with col2:
    st.subheader("Guía educativa")
    concepto = st.text_input("Concepto (ej: Funciones continuas)", "Funciones continuas")
    if st.button("Generar guía (.md)"):
        vs = load_or_create_vs(uploaded_pdf)
        retriever = vs.as_retriever(search_kwargs={"k": 6})
        ctx_docs = retriever.get_relevant_documents(concepto)
        ctx = "\n\n".join(d.page_content for d in ctx_docs)

        guide = llm.invoke(guide_prompt.format(concepto=concepto, context=ctx)).content
        fname = f"guia_{concepto.lower().replace(' ','_')}_{uuid.uuid4().hex[:6]}.md"
        st.download_button("Descargar guía", guide.encode("utf-8"), file_name=fname, mime="text/markdown")
        st.success("Guía generada. Revisa las citas [PAG N].")
