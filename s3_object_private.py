import boto3

s3 = boto3.client("s3")

for bucket in s3.list_buckets()["Buckets"]:
    bucket_name = bucket["Name"]

    if bucket_name == "100daysofdevops.com":
      all_objects = s3.list_objects(Bucket=bucket_name)
      for obj in all_objects["Contents"]:
        bucket_key = obj["Key"]

        response = s3.get_object_acl(Bucket=bucket_name, Key=bucket_key)
        if len(response["Grants"]) > 1:
          print(f"The bucket {bucket_name} with key {bucket_key} is now marked as private")
          s3.put_object_acl(Bucket=bucket_name, Key=bucket_key, ACL="private") 