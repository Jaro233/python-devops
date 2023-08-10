import re
from collections import Counter
import csv
import argparse


my_parser = argparse.ArgumentParser(description="Reading the log file")
my_parser.add_argument("logfile",help="Please enter the logfile to parse", type=argparse.FileType("r"))
args = my_parser.parse_args()

logreg = r"\b(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\b"

def read_file(logfile):
  with args.logfile as file:
    logs = file.read()
    ip_list = re.findall(logreg, logs)
    return ip_list

def read_count():
  ip_list = read_file(args.logfile)
  ip_count = Counter(ip_list)
  return ip_count

def csv_write():
  ip_count = read_count()
  with open("ipcount.csv", "w") as file:
    file_writer = csv.writer(file)
    file_writer.writerow(["IP Address", "Count"])
    for k, v in ip_count.items():
      file_writer.writerow([k, v])

if __name__ == "__main__":
  csv_write()