import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("NYT_KEY")
test = requests.get(
    f"https://api.nytimes.com/svc/archive/v1/2019/1.json?api-key={API_KEY}"
)

print(test.text)
