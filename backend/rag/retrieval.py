from rag.embeddings import get_embeddings
from db import db

def retrieve_context(query: str, top_k: int = 3) -> str:
    """
    Retrieves relevant policy context for the given query.
    If database is not connected, returns a fallback message.
    """
    if not db.is_configured:
        return "No policy database connected. General knowledge applies."
        
    query_embedding = get_embeddings(query)
    
    # In the future: Execute pgvector similarity search here using query_embedding
    # For MVP without connected db:
    return "Mock context from retrieved documents."
