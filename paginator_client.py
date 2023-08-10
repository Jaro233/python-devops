import boto3

client = boto3.client("iam")

paginator = client.get_paginator('list_users')
page_iterator = paginator.paginate()

count = 1

for user in page_iterator:
    for username in user["Users"]:
        print(count, username["UserName"])
        count += 1

# for user in client.list_users()["Users"]:
#     print(count, user["UserName"])
#     count += 1