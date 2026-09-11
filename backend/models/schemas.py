from pydantic import BaseModel

class HealthQuery(BaseModel):
    question: str
