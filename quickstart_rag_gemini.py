import os, time, uuid
from dotenv import load_dotenv
from pypdf import PdfReader

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnableParallel, RunnablePassthrough

load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")
assert API_KEY, "Falta GOOGLE_API_KEY en .env"

DATA_PATH = "data/matematicas.pdf"
INDEX_DIR = "vectorstore"

# ---------- 1) Cargar y trocear PDF ----------
def load_pdf_text(path):
    reader = PdfReader(path)
    texts = []
    for i, page in enumerate(reader.pages):
        t = page.extract_text() or ""
        if t.strip():
            texts.append(f"[PAG {i+1}]\n{t}")
    return "\n\n".join(texts)

raw_text = load_pdf_text(DATA_PATH)

splitter = RecursiveCharacterTextSplitter(
    chunk_size=900, chunk_overlap=150, separators=["\n\n", "\n", " ", ""]
)
docs = splitter.create_documents([raw_text])

# ---------- 2) Embeddings + FAISS ----------
emb = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")
if not os.path.exists(INDEX_DIR):
    os.makedirs(INDEX_DIR, exist_ok=True)
    vs = FAISS.from_documents(docs, emb)
    vs.save_local(INDEX_DIR)
else:
    vs = FAISS.load_local(INDEX_DIR, emb, allow_dangerous_deserialization=True)

retriever = vs.as_retriever(search_kwargs={"k": 4})

# ---------- 3) Modelo Gemini ----------
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    temperature=0.2,
)

# ---------- 4) Prompt para RAG ----------
RAG_TEMPLATE = """Eres un profesor de matematicas. Responde con claridad y rigor.
Usa EXCLUSIVAMENTE el contexto si es suficiente; si no lo es, dilo.
Incluye referencias [PAG N] de donde sacaste la info.

Pregunta del usuario: {question}

Contexto:
{context}

Respuesta (clara, con pasos si aplica):"""

rag_prompt = PromptTemplate.from_template(RAG_TEMPLATE)

def format_docs(docs):
    return "\n\n".join(d.page_content for d in docs)

rag_chain = (
    RunnableParallel({"context": retriever | format_docs, "question": RunnablePassthrough()})
    | rag_prompt
    | llm
)

# ---------- 5) Prompt para guia educativa ----------
GUIDE_TEMPLATE = """Genera una guia educativa en Markdown sobre el concepto: "{concepto}".
Estructura:
# {concepto}
## Definicion
(3-5 lineas, claro y formal)

## Ejemplo sencillo (paso a paso)
- Planteamiento
- Desarrollo
- Resultado

## Ejemplo avanzado (paso a paso)
- Planteamiento
- Desarrollo
- Resultado

## 3 ejercicios propuestos
1) ...
2) ...
3) ...

## Soluciones
- Ejercicio 1: ...
- Ejercicio 2: ...
- Ejercicio 3: ...

Usa el siguiente contexto del material como fuente principal y cita [PAG N] donde corresponda.
Contexto:
{context}
"""
guide_prompt = PromptTemplate.from_template(GUIDE_TEMPLATE)

def build_guide(concepto: str):
    ctx_docs = retriever.get_relevant_documents(concepto)
    ctx = format_docs(ctx_docs)
    return llm.invoke(guide_prompt.format(concepto=concepto, context=ctx)).content

# ---------- 6) Demostracion ----------
if __name__ == "__main__":
    pregunta = "Que es una funcion continua y cuales son sus propiedades clave?"
    t0 = time.perf_counter()
    resp = rag_chain.invoke(pregunta)
    dt = time.perf_counter() - t0

    print("\n=== RESPUESTA RAG ===\n")
    print(resp.content)
    print(f"\n[latencia: {dt:.2f}s]")

    concepto = "Funciones continuas"
    guia_md = build_guide(concepto)
    out_path = f"guia_{uuid.uuid4().hex[:8]}.md"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(guia_md)
    print(f"\nGuia generada: {out_path}")