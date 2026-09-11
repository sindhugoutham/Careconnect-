# CareConnect

AI-powered healthcare navigation and policy assistant.

## Architecture

- `frontend/` — React + Vite user interface
- `backend/` — FastAPI backend
- `backend/routes/` — API endpoints
- `backend/rag/` — document chunking, embeddings, retrieval
- `backend/models/` — database/data schemas

## Run locally

### Backend
```bash
cd backend
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

Never commit real API keys or `.env` files.
