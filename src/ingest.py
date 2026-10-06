import os

api_key = os.getenv("TIINGO_API_KEY")

if api_key:
    print("TIINGO_API_KEY recibida correctamente")
else:
    print("TIINGO_API_KEY no encontrada")
