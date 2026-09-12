from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import ask_policy, checklist, find_care

app = FastAPI(title="CareConnect API", version="0.1.0")

# CORS Configuration for the React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"], # default Vite and CRA ports
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ask_policy.router)
app.include_router(checklist.router)
app.include_router(find_care.router)

@app.get("/health")
def health():
    return {"status": "ok", "service": "careconnect"}
