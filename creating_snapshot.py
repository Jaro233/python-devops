import boto3

ec2 = boto3.resource("ec2")

for vol in ec2.volumes.all():
    vol_id = vol.id
    volume = ec2.Volume(vol_id)
    desc = f"This is the snapshot of {vol_id}"
    print(f"Creating the snapshot of the following Volume: {vol_id}")
    volume.create_snapshot(Description=desc)