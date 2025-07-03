import requests
import os

URL = "https://apiking.onrender.com/health"
TOKEN = os.environ.get("PING_TOKEN")

try:
    response = requests.get(f"{URL}?pingToken={TOKEN}", timeout=5)
    print(f"Ping status: {response.status_code}")
except Exception as e:
    print(f"Ping failed: {e}")
