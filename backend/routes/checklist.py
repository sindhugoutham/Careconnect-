from fastapi import APIRouter

router = APIRouter(prefix="/api/checklist", tags=["checklist"])

@router.get("/")
def get_checklist():
    return {"items": []}
