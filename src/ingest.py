import requests
import os
from supabase import create_client

api_key = os.getenv("TIINGO_API_KEY")
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")


supabase = create_client(supabase_url, supabase_key)

response = supabase.table("stock_prices").select("id").limit(1).execute()

print("Conexión con Supabase correcta")


