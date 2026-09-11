from fastapi import APIRouter

router = APIRouter(prefix="/api/policy", tags=["policy"])

@router.post("/ask")
def ask_policy(question: str):
    return {"question": question, "answer": "Policy assistant endpoint ready."}
