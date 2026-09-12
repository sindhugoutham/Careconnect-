import os
import requests
from dotenv import load_dotenv

load_dotenv()

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

def get_embeddings(text: str, model: str = "nomic-embed-text") -> list[float]:
    """
    Uses Ollama's local embeddings API to generate vector embeddings.
    Make sure to run `ollama pull nomic-embed-text` to use this free local model.
    """
    try:
        url = f"{OLLAMA_BASE_URL}/api/embeddings"
        payload = {
            "model": model,
            "prompt": text
        }
        response = requests.post(url, json=payload, timeout=30)
        if response.status_code == 404:
            raise Exception(f"Model '{model}' not found in Ollama. Run `ollama pull {model}`.")
        response.raise_for_status()
        data = response.json()
        return data.get("embedding", [])
    except Exception as e:
        print(f"Embedding error: {str(e)}")
        return []
