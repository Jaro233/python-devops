import boto3

ec2 = boto3.resource("ec2")

regions = []
for region in ec2.meta.client.describe_regions()["Regions"]:
    regions.append(region["RegionName"])

for region in regions:
    ec2 = boto3.resource("ec2", region_name=region)
    print("EC2 regions: ", region)

    ec2_filter = {"Name": "instance-state-name", "Values": ["running"]}

    instances = ec2.instances.filter(Filters=[ec2_filter])

    for instance in instances:
        instance.stop()
        print("The following instance is now in stopped state", instance.id)

# print(regions)
# ec2_filter = {"Name": "instance-type", "Values": ["t2.micro"]}
# ec2_tag = {"Name": "tag:Name", "Values": ["boto3-prod"]}
# for instance in ec2.instances.filter(Filters=[ec2_tag]):
#     instance.stop()