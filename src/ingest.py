import requests

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

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Token 66ffa5b0f9e8f557ad2d9e0137c110dd2b7734df'
}
all_data=[]

for ticker in tickers:

    url=f'https://api.tiingo.com/tiingo/daily/{ticker}/prices?startDate=2000-1-1'

    response=requests.get(url, headers=headers)
    data=response.json()

    clean_data = [
        {
            "ticker": f'{ticker}',
            "date": row["date"],
            "open": row["open"],
            "high": row["high"],
            "low": row["low"],
            "close": row["close"],
            "volume": row["volume"]
        }
        for row in data]
    all_data.extend(clean_data)

