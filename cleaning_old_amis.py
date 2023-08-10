import boto3
import datetime
from dateutil.parser import parse

client = boto3.client("ec2")
current_date = datetime.datetime.now()
max_ami_age = 1


my_ami = client.describe_images(Owners=["self"])["Images"]

for ami in my_ami:
    creation_date = ami["CreationDate"]
    creation_date_parse = parse(creation_date).replace(tzinfo=None)
    ami_id = ami["ImageId"]
    diff_in_days = (current_date - creation_date_parse).days
    if diff_in_days > max_ami_age:
        print("Cleaning old ami's greater than 1 days old", ami_id)
        client.deregister_image(
            ImageId=ami_id,
            DryRun=True
        )