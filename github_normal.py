import requests
import os
import json

token = os.environ.get("GITHUB_TOKEN")

# reponame = input("Please enter the repo name you want to create: ")
# reponame = input("Please enter the repo name you want to delete: ")
GITHUB_API_URL = "https://api.github.com/"
# headers = {"Authorization": f"token {token}"}
# data = {"name": f"{reponame}"}

# r = requests.post(GITHUB_API_URL + "user/repos", data=json.dumps(data), headers=headers)
# print(r)

# username = input("Please enter your Github username: ")
# r = requests.delete(GITHUB_API_URL + f"repos/{username}/{reponame}", headers=headers)
# print(r)

data = {"type": "all", "sort": "full_name", "direction": "asc"}
username = input("Please enter yout Github username: ")
output = requests.get(GITHUB_API_URL + f"users/{username}/repos", data=json.dumps(data))
output = json.loads(output.text)

for reponame in output:
    print(reponame["name"])