import requests

# Page-based pagination — fetching all posts 5 at a time
BASE_URL = "https://jsonplaceholder.typicode.com/posts"
PAGE_SIZE = 5
all_posts = []
page = 1

print("Fetching posts page by page...\n")

while True:
    params = {
        "_page": page,
        "_limit": PAGE_SIZE
    }

    response = requests.get(BASE_URL, params=params)
    
    if response.status_code != 200:
        print(f"Error on page {page}: {response.status_code}")
        break

    posts = response.json()

    if not posts:
        print(" No more pages  we've fetched everything!")
        break

    all_posts.extend(posts)
    print(f"  Page {page}: fetched {len(posts)} posts (total so far: {len(all_posts)})")
    print(posts)

    if page >= 3:
        print("  (Stopping at page 3 for demo purposes...)")
        break

    page += 1

print(f"\n Total posts fetched: {len(all_posts)}")