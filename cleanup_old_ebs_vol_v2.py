import boto3

ec2 = boto3.resource("ec2")

vol_status = {'Name': "status", "Values": ["available"]}

def get_all_regions():
    regions = []
    for region in ec2.meta.client.describe_regions()["Regions"]:
        regions.append(region["RegionName"])
    return regions

def cleanup_ebs_vol():
  regions = get_all_regions()
  for region in regions:
    ec2 = boto3.resource("ec2", region_name=region)
    for vol in ec2.volumes.filter(Filters=[vol_status]):
        vol_id = vol.id
        volume = ec2.Volume(vol_id)
        print(f"Cleanup EBS Volume with id {vol_id} in region {region}")
        volume.delete()

if __name__ == "__main__":
  cleanup_ebs_vol()