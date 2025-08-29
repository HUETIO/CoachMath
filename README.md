# RAG Matem�ticas con Gemini echo por Diego Sepulveda (DASH) ByReaper.
"#$%%&$/&$%#$#"#$%$%&%/&/$%&#$"#"

Aplicaci�n Streamlit para responder preguntas y generar gu�as educativas de matem�ticas usando RAG y Gemini.

## Requisitos

- Python 3.9 o superior
- Archivo PDF de matem�ticas (`data/matematicas.pdf`) o tu propio PDF
- Clave de API de Google Gemini

## Instalaci�n

1. **Clona el repositorio**  
   ```bash
   git clone https://github.com/tu_usuario/rag-matematicas-gemini.git
   ```
2. **Entra en la carpeta**  
   ```bash
   cd rag-matematicas-gemini
   ```
3. **Instala las dependencias**  
   ```bash
   pip install -r requirements.txt
   ```
4. **Coloca tu PDF**  
   - Usa el archivo por defecto `data/matematicas.pdf`  
   - O sube tu propio PDF desde la interfaz

## Ejecuci�n

```bash
streamlit run app.py
```

## Uso

- **Chat RAG:** Haz preguntas sobre matem�ticas y obt�n respuestas con referencias al PDF.
- **Gu�a educativa:** Genera gu�as en Markdown sobre conceptos matem�ticos, con ejemplos y ejercicios.

## Notas

- Si no se encuentra la variable `GOOGLE_API_KEY` en `.env`, la aplicaci�n no iniciar�.
- Puedes ajustar la creatividad del modelo desde la barra lateral.
- Las gu�as generadas pueden descargarse en formato `.md`.