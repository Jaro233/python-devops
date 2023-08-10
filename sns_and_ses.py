import boto3

ec2 = boto3.resource("ec2")
client = boto3.client("ses")
# client = boto3.client("sns")
# topic = client.create_topic(
#     Name='sns-demo'
# )

email = "jaroslaw.waliczek@vp.pl"
# response = client.subscribe(TopicArn=topic["TopicArn"], Protocol="email", Endpoint=email, ReturnSubscriptionArn=True)

vol_status = {'Name': "status", "Values": ["available"]}

for vol in ec2.volumes.filter(Filters=[vol_status]):
    vol_id = vol.id
    volume = ec2.Volume(vol_id)
    print("Cleanup EBS Volume: ", vol_id)
    volume.delete()

    msg = f"Following EBS Volume {vol_id} is deleted"
    # client.publish(TopicArn=topic["TopicArn"], Message=msg)

    client.send_email(
        Source=email,
        Destination={
            'ToAddresses': [
                email
            ],
        },
        Message={
            'Subject': {
                'Data': f"Cleanup EBS Volume: {vol_id}"
            },
            'Body': {
                'Text': {
                    'Data': msg,
                },
            }
        }
    )