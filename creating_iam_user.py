import boto3
import argparse
import string
import secrets
import sys

iam = boto3.client("iam")

def random_password(length=16):
  # Generate a random password with specified length
  chars = string.ascii_letters + string.digits + string.punctuation
  password = ""
  for i in range(length):
    password += secrets.choice(chars)
  return password

def create_iam_user(username, password=None, attach_policy=None):
  try:
    iam.get_user(UserName=username)
    print(f"User {username} already exists")
  except iam.exceptions.NoSuchEntityException as e:
    try:
      if password == None:
        password = random_password()
      iam.create_user(UserName=username)
      iam.create_login_profile(UserName=username, Password=password, PasswordResetRequired=True)
      print(f"User {username} created successfully with password {password}")
      if attach_policy == None:
        iam.attach_user_policy(UserName=username, PolicyArn="arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess")
        print(f"S3 read only policy attached to user: {username}")
    except Exception as e:
      print(f"Error creating user")

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Creating an IAM user")
  parser.add_argument("--username", type=str, help="Name of the IAM user that you want to create")
  parser.add_argument("--password", type=str, help="Password for the IAM user (if you don't provide it, than a random password wii be generated)")
  parser.add_argument("--attach_policy", type=str, help="Attach an IAM policy to the user")
  parser.add_argument("--filename", type=str, help="Filename that contains IAM users, seperated by line")

  args = parser.parse_args()

  if not any(vars(args).values()):
    parser.print_help()
    sys.exit()

  if args.filename:
    with open(args.filename, "r") as file:
      usernames = file.read().splitlines()
      for username in usernames:
        create_iam_user(username, args.password, args.attach_policy)
  else:      
    create_iam_user(args.username, args.password, args.attach_policy)