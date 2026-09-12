# CareConnect

CareConnect is a modern, AI-powered healthcare navigation and policy assistant. 
It helps users understand healthcare policies through an AI assistant, find local care options based on specialty/location, and manage their health journey with an interactive checklist.

## Architecture

**Frontend:** React (Vite), plain CSS
**Backend:** FastAPI, Python, Pydantic
**AI Engine:** Ollama (local LLM generation and embeddings)
**RAG (Retrieval-Augmented Generation):** Custom pipeline for chunking and retrieval (prepared for Supabase pgvector)
**Database:** Supabase PostgreSQL (via environment variables, handles graceful fallback if not configured)

## Folder Structure

```
careconnect/
├── frontend/             # React application (Vite)
│   ├── src/
│   │   ├── api/          # API hooks for backend communication
│   │   ├── components/   # UI components (Header, Hero, FindCare, PolicyAssistant, Checklist)
│   │   ├── App.jsx       # Main layout and routing
│   │   └── styles.css    # Global styling
│   └── package.json
├── backend/              # FastAPI Application
│   ├── main.py           # Entry point and CORS
│   ├── db.py             # Database configuration (Supabase)
│   ├── models/           # Pydantic schemas (HealthQuery, FindCareQuery)
│   ├── rag/              # Local RAG pipeline (document_loader, chunking, embeddings, retrieval)
│   ├── routes/           # API routes (policy, care, checklist)
│   └── services/         # External integrations (ollama.py)
├── .env.example          # Environment variable template
└── README.md
```

## Local Setup Instructions

### Environment Variables
1. Copy `.env.example` to `.env`.
   ```bash
   cp .env.example .env
   ```
2. By default, `OLLAMA_BASE_URL` is set to `http://localhost:11434`.
3. Supabase credentials (`SUPABASE_URL`, `DATABASE_URL`) are optional for local development.

### Ollama Setup (Free Local AI)
1. Download and install [Ollama](https://ollama.com/).
2. Pull the required models:
   ```bash
   ollama pull qwen2.5:7b       # For AI generation
   ollama pull nomic-embed-text # For RAG embeddings
   ```
3. Keep Ollama running in the background.

### Backend Setup
```bash
cd backend
python -m venv venv
venv\Scripts\activate      # Windows
# source venv/bin/activate # Mac/Linux
pip install -r requirements.txt httpx
uvicorn main:app --reload
```
The API runs at `http://localhost:8000`.

### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```
The React app runs at `http://localhost:5173`.

## API Endpoints
- `GET /health` - API status
- `POST /api/policy/ask` - Send a policy question to the Ollama AI
- `POST /api/care/find` - Search for mock healthcare providers by location and need
- `GET /api/checklist` - Get interactive health checklist items

## Current Limitations
- Healthcare provider search currently uses heavily marked **mock data** pending connection to a real provider database or API.
- The RAG system handles embedding through Ollama but mock retrieves context until the database (Supabase pgvector) is fully connected.
