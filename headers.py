import requests
import os
from dotenv import load_dotenv

load_dotenv()
AUTH_TOKEN = os.getenv("AUTH_KEY")

#AUTH_TOKEN = "my_secret_token_abc123"  
print(AUTH_TOKEN)
headers = {
    "Authorization": f"Bearer {AUTH_TOKEN}",   # authentication
    "Content-Type": "application/json",         # type of the payload
}

payload = {
    "title": "Secure Post",
    "body": "This post was made with auth headers.",
    "userId": 42
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts", 
    json=payload,
    headers=headers
)

print("Status Code:", response.status_code)
print("Request Headers Sent:", dict(response.request.headers))
print("Response:", response.json())