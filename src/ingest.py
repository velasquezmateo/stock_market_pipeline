import requests
import os
from supabase import create_client

api_key = os.getenv("TIINGO_API_KEY")
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")

supabase = create_client(supabase_url, supabase_key)

headers = {
    "Authorization": f"Token {api_key}"
}

all_data=[]

tickers=["AAPL",
    "MSFT",
    "NVDA",
    "AMZN",
    "GOOGL",
    "JPM",
    "XOM",
    "JNJ",
    "KO",
    "CAT"]

start_date=(datetime.now()-timedelta(days=2)).strftime("%Y-%m-%d")

for ticker in tickers:

    url=f'https://api.tiingo.com/tiingo/daily/{ticker}/prices?startDate={start_date}'

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
    .upsert(all_data, on_conflict="ticker,date").execute()
)



