import boto3
import datetime
from dateutil.parser import parse

client = boto3.client("ec2")
current_time = datetime.datetime.now()
max_ami_age = 1

def get_all_regions():
  regions = []
  r = client.describe_regions()
  for region in r["Regions"]:
    regions.append(region["RegionName"])
  # print(regions)
  return regions

def calc_time_diff():
  regions = get_all_regions()
  for region in regions:
    client = boto3.client("ec2", region_name=region)
    my_amis = client.describe_images(Owners=["self"])
    for ami in my_amis["Images"]:
      creation_date = ami["CreationDate"]
      ami_id = ami["ImageId"]
      parsed_creation_date = parse(creation_date).replace(tzinfo=None)
      time_diff = (current_time - parsed_creation_date).days
      # print(time_diff, ami_id, region)
      clean_ami(time_diff, ami_id, region, client)

def clean_ami(time_diff, ami_id, region, client):
  if time_diff > max_ami_age:
    client.deregister_image(
        ImageId=ami_id,
        DryRun=False
    )
    print(f"Ami in region {region} with id {ami_id} is cleaned")

if __name__ == "__main__":
  calc_time_diff()
