# RAG Matemáticas con Gemini echo por Diego Sepulveda (DASH) ByReaper.
"#$%%&$/&$%#$#"#$%$%&%/&/$%&#$"#"

Aplicación Streamlit para responder preguntas y generar guías educativas de matemáticas usando RAG y Gemini.

## Requisitos

- Python 3.9 o superior
- Archivo PDF de matemáticas (`data/matematicas.pdf`) o tu propio PDF
- Clave de API de Google Gemini

## Instalación

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

## Ejecución

```bash
streamlit run app.py
```

## Uso

- **Chat RAG:** Haz preguntas sobre matemáticas y obtén respuestas con referencias al PDF.
- **Guía educativa:** Genera guías en Markdown sobre conceptos matemáticos, con ejemplos y ejercicios.

## Notas

- Si no se encuentra la variable `GOOGLE_API_KEY` en `.env`, la aplicación no iniciará.
- Puedes ajustar la creatividad del modelo desde la barra lateral.
- Las guías generadas pueden descargarse en formato `.md`.