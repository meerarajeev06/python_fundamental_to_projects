import requests

a = input("Github Username : ")
url = "https://api.github.com/users/{a}"
response = requests.get(url)

data = response.json()

print(f"Name: {data.get('name','N/A')}")
print(f"Location: {data.get('location','N/A')}")
print(f"Repositories: {data.get('public_repos',0)}")
print(f"Followers: {data.get('followers',0)}")