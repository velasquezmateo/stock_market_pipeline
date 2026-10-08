import requests
import os
from supabase import create_client

api_key = os.getenv("TIINGO_API_KEY")
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")

headers = {
    "Authorization": f"Token {api_key}"
}

all_data=[]

for ticker in tickers:

    url=f'https://api.tiingo.com/tiingo/daily/{ticker}/prices?startDate=2000-1-1'

    response=requests.get(url, headers=headers)
    data=response.json()

    clean_data = [
        {
            "ticker": f'{ticker}',
            "date": row["date"][:10],
            "open": row["open"],
            "high": row["high"],
            "low": row["low"],
            "close": row["close"],
            "volume": row["volume"]
        }
        for row in data]
    all_data.extend(clean_data)

db_supabase = (
    supabase
    .table("stock_prices")
    .upsert(
        all_data,
        on_conflict="ticker,date"
    )
    .execute()
)

print("Registros enviados:", len(all_data))

