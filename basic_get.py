import requests

# Basic GET request
#path_param = {"id": 1, "userId" : 2}
response = requests.get(f"https://jsonplaceholder.typicode.com/users")



print("Status Code:", response.status_code)
print('####################################')
print('########################################')
#print("Response JSON:", response.json())
#print(response.url)
#print(response.text)
data = response.json()

for user in data:
    print(f'Name  - {user['name']} , email  - {user['email']}' )



#pip install requests 