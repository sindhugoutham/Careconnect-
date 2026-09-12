from pydantic import BaseModel

class HealthQuery(BaseModel):
    question: str

class FindCareQuery(BaseModel):
    location: str
    need: str
