from fastapi import APIRouter
from models.schemas import FindCareQuery

router = APIRouter(prefix="/api/care", tags=["care"])

@router.post("/find")
def find_care(query: FindCareQuery):
    # Mock data for frontend development
    results = [
        {"id": 1, "name": "General Hospital (Mock Data)", "type": "Hospital", "address": f"123 Health St, {query.location}", "specialty": query.need},
        {"id": 2, "name": "Dr. Smith Clinic (Mock Data)", "type": "Primary Care", "address": f"456 Wellness Blvd, {query.location}", "specialty": "General Medicine"}
    ]
    return {"query": query.model_dump(), "results": results}
