import os
import requests
from dotenv import load_dotenv

load_dotenv()

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

class OllamaService:
    def __init__(self, base_url: str = OLLAMA_BASE_URL):
        self.base_url = base_url

    def generate(self, prompt: str, model: str = "qwen2.5:7b") -> str:
        """
        Sends a prompt to the local Ollama instance and returns the generated text.
        """
        try:
            url = f"{self.base_url}/api/generate"
            payload = {
                "model": model,
                "prompt": prompt,
                "stream": False
            }
            response = requests.post(url, json=payload, timeout=60)
            
            if response.status_code == 404:
                raise Exception(f"Model '{model}' not found in Ollama. Please ensure it is pulled.")
                
            response.raise_for_status()
            data = response.json()
            return data.get("response", "")
        except requests.exceptions.ConnectionError:
            raise Exception(f"Failed to connect to Ollama at {self.base_url}. Is the service running?")
        except requests.exceptions.Timeout:
            raise Exception("Request to Ollama timed out.")
        except Exception as e:
            raise Exception(f"Error communicating with Ollama: {str(e)}")
