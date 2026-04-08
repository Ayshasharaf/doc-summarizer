# Document Summarizer API

An AI-powered REST API that summarizes text and PDF documents using NLP models.

## Tech Stack
- **FastAPI** — REST API framework
- **Hugging Face** — BART summarization model
- **Docker** — Containerized deployment
- **Python** — Core language

## Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | Health check |
| POST | `/summarize/text` | Summarize raw text |
| POST | `/summarize/file` | Summarize a PDF file |

## Run Locally

### Without Docker
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### With Docker
```bash
docker build -t doc-summarizer .
docker run -p 8000:8000 --env-file .env doc-summarizer
```

## Environment Variables
