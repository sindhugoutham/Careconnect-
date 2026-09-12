import os
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL", "")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "")
DATABASE_URL = os.getenv("DATABASE_URL", "")

class DatabaseConfig:
    def __init__(self):
        self.is_configured = bool(SUPABASE_URL and SUPABASE_KEY) or bool(DATABASE_URL)

    def get_connection(self):
        """
        Placeholder for database connection logic using asyncpg or SQLAlchemy.
        Will be used for pgvector setup.
        Returns None if not configured, allowing app to gracefully fall back to mock data.
        """
        if not self.is_configured:
            print("Warning: Database credentials not provided. Falling back to mock data where applicable.")
            return None
        
        # In the future: return actual engine/connection here
        return "MOCK_CONNECTION"

db = DatabaseConfig()
