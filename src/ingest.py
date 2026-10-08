import requests
import os

supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_SECRET_KEY")

print("SUPABASE_URL recibida:", bool(supabase_url))
print("SUPABASE_KEY recibida:", bool(supabase_key))


