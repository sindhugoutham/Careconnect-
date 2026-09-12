from fastapi import APIRouter, HTTPException
from models.schemas import HealthQuery
from services.ollama import OllamaService
from rag.retrieval import retrieve_context

router = APIRouter(prefix="/api/policy", tags=["policy"])
ollama_service = OllamaService()

@router.post("/ask")
def ask_policy(query: HealthQuery):
    # Retrieve context from pgvector/RAG
    context = retrieve_context(query.question)
    
    prompt = f"Context: {context}\n\nAnswer this healthcare policy question based on the context if applicable: {query.question}"
    
    # We call Ollama
    try:
        answer = ollama_service.generate(prompt, model="qwen2.5:7b")
        return {"question": query.question, "answer": answer}
    except Exception as e:
        raise HTTPException(status_code=503, detail=str(e))
