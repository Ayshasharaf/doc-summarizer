import pypdf
import io

def extract_text_from_pdf(file_bytes: bytes) -> str:
    pdf_reader = pypdf.PdfReader(io.BytesIO(file_bytes))
    text = ""
    for page in pdf_reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted + "\n"  # avoid pages bleeding into each other
    if not text.strip():
        raise ValueError("Could not extract text from PDF")
    return text