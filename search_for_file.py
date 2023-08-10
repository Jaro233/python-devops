import os
import argparse

parser = argparse.ArgumentParser(description='Reading the directory path to find the file')
parser.add_argument('pathname', help='Please enter the directory path')
parser.add_argument('filesearch', help='Please enter the filename to search')

args = parser.parse_args()

for dirpath, dirnames, filenames in os.walk(args.pathname):
  for file in filenames:
    if file == args.filesearch:
      print(os.path.join(dirpath, file))