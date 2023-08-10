import boto3

ec2 = boto3.resource("ec2")

instance = ec2.Instance("i-0b273423df1d19f27")

# print(instance.state["Name"])

# print("Starting EC2 Instance")
print("Stopping EC2 Instance")
# instance.start()
instance.stop()
instance.wait_until_stopped()
# print("EC2 Instance started")
print("EC2 Instance stopped")