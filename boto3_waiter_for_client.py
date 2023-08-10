import boto3

client = boto3.client("ec2")

print("Starting EC2 Instance")
client.start_instances(InstanceIds=["i-0b273423df1d19f27"])

waiter = client.get_waiter("instance_running")

waiter.wait(InstanceIds=["i-0b273423df1d19f27"])

print("EC2 Instance started")