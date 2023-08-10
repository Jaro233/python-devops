import os
import pathlib

'''
FileNotFoundError
PermissionError:
IsADirectoryError:
'''
# try:
#   open("e:\python-devops")
# except Exception as e:
#   print(e)

# print(os.path.exists("e:\python-devops"))
# print(os.path.isfile("e:\python-devops"))
# print(os.path.isdir("e:\python-devops"))

# filename="e:\python-devops\\test"

# if os.path.exists(filename) and os.path.isfile(filename):
#   print("File exist")
# else:
#   print("File doesn't exist")

path = pathlib.Path("e:\python-devops\\test")
print(path.exists())
print(path.is_file())
print(path.is_dir())
