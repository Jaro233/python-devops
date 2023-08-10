from github import Github
import os

access_token = os.environ.get("GITHUB_TOKEN")

g=Github(access_token)
# for repo in g.get_user().get_repos():
#   print(repo.name)

repo = g.get_repo("Jaro233/cicd-kube-docker-v2")
print(list(repo.get_branches()))