import boto3
import datetime

client = boto3.client("iam")

paginator = client.get_paginator('list_users')

current_date = datetime.datetime.now(datetime.timezone.utc)
max_key_age = 5

for response in paginator.paginate():
    for user in response["Users"]:
        username = user["UserName"]

        list_key = client.list_access_keys(UserName=username)

        for access_key in list_key["AccessKeyMetadata"]:
            access_key_id = access_key["AccessKeyId"]
            key_creation_date = access_key["CreateDate"]

            age = (current_date - key_creation_date).days
            if age > max_key_age:
                print("Deactivating Key for the following user: ", username)
                client.update_access_key(
                    AccessKeyId=access_key_id,
                    Status='Inactive',
                    UserName=username,
                )

