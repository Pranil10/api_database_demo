import requests

# GET with query parameters
params = {
    "userId": 2,      
    "_limit": 3       
}

response = requests.get(
    "https://jsonplaceholder.typicode.com/posts",
    params=params
)

print("URL called:", response.url)

posts = response.json()
for post in posts:
    print(f"  Post ID: {post['id']} | Title: {post['title'][:40]}...")