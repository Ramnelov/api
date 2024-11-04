import os

from dotenv import load_dotenv
from supabase.client import Client, create_client

load_dotenv()

url: str = os.environ.get("SUPABASE_URL", "")
key: str = os.environ.get("SUPABASE_KEY", "")

if not url or not key:
    raise ValueError(
        "SUPABASE_URL and SUPABASE_KEY must be set in the environment variables"
    )

supabase: Client = create_client(url, key)
