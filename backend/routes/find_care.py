from fastapi import APIRouter

router = APIRouter(prefix="/api/care", tags=["care"])

@router.get("/")
def find_care(query: str = ""):
    return {"query": query, "results": []}
