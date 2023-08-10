import boto3

iam = boto3.resource("iam")

count = 1
for user in iam.users.all():
    print(count, user.name)
    count += 1