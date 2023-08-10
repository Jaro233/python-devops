import re
from collections import Counter
import csv
import argparse


my_parser = argparse.ArgumentParser(description="Reading the log file")
my_parser.add_argument("logfile",help="Please enter the logfile to parse", type=argparse.FileType("r"))
args = my_parser.parse_args()

logfile="access_logs.txt"

# logreg = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

logreg = r"\b(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\b"

with args.logfile as file:
  file_read = file.read()
  ip_list = re.findall(logreg, file_read)
  print(ip_list)
  with open("ipcount.csv", "w") as file:
    file_writer_csv = csv.writer(file)
    file_writer_csv.writerow(["IP_Address", "Count"])
    for k, v in Counter(ip_list).items():
      file_writer_csv.writerow([k, v])




# grep -Po "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}" access_logs.txt | sort | uniq -c
# lepszy regex grep -Po '\b(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\b' ip