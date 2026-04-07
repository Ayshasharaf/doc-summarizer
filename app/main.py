from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
from app.summarizer import summarize_text
from app.utils import extract_text_from_pdf

app = FastAPI(title="Document Summarizer API")

MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB

class TextInput(BaseModel):
    text: str

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/summarize/text")
def summarize_text_endpoint(body: TextInput):
    if not body.text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty")
    try:
        summary = summarize_text(body.text)
    except RuntimeError as e:
        raise HTTPException(status_code=502, detail=str(e))
    return {"summary": summary}

@app.post("/summarize/file")
async def summarize_file_endpoint(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files supported")
    
    contents = await file.read()

    if len(contents) > MAX_FILE_SIZE:
        raise HTTPException(status_code=413, detail="File too large (max 5MB)")

    try:
        text = extract_text_from_pdf(contents)
        summary = summarize_text(text)
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
    except RuntimeError as e:
        raise HTTPException(status_code=502, detail=str(e))

    return {"summary": summary}