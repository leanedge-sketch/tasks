"""Load environment variables and initialize the Supabase client."""

from __future__ import annotations

import os
from typing import Optional

from dotenv import load_dotenv
from supabase import Client, create_client

load_dotenv()

_url = os.getenv("SUPABASE_URL", "").strip()
_key = os.getenv("SUPABASE_KEY", "").strip()

supabase: Optional[Client]
if _url and _key:
    supabase = create_client(_url, _key)
else:
    supabase = None
