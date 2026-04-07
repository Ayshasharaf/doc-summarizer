import os
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

load_dotenv()

client = InferenceClient(
    provider="hf-inference",
    api_key=os.environ["HF_API_KEY"],
)

def summarize_text(text: str) -> str:
    if len(text.split()) > 800:
        text = " ".join(text.split()[:800])

    try:
        result = client.summarization(
            text,
            model="facebook/bart-large-cnn",
           
        )
        return result.summary_text
    except Exception as e:
        raise RuntimeError(f"Summarization failed: {str(e)}")