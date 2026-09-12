from fastapi import APIRouter

router = APIRouter(prefix="/api/checklist", tags=["checklist"])

@router.get("/")
def get_checklist():
    # Mock data for frontend development
    items = [
        {"id": 1, "task": "Review current insurance policy", "completed": False},
        {"id": 2, "task": "Find a primary care physician", "completed": False},
        {"id": 3, "task": "Schedule annual physical exam", "completed": False}
    ]
    return {"items": items}
