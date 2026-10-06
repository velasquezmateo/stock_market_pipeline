import os
import requests

api_key = os.getenv("TIINGO_API_KEY")

url = "https://api.tiingo.com/tiingo/daily/AAPL/prices"

headers = {
    "Authorization": f"Token {api_key}"
}

response = requests.get(url, headers=headers)

print("Status code:", response.status_code)
