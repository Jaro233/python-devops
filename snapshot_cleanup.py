import boto3
import datetime

ec2 = boto3.resource("ec2")
current_date = datetime.datetime.now(tz=datetime.timezone.utc)
diff_date = current_date - datetime.timedelta(days=6)

snapshots = ec2.snapshots.filter(OwnerIds=["self"])

for snapshot in snapshots:
    snapshot_start_time = snapshot.start_time 
    if diff_date > snapshot_start_time:
        try:
            print(f"Deleting snapshot: {snapshot.id}")
            snapshot.delete()
        except Exception as e:
            print(f"Current snapshot is in use: {snapshot.id}")