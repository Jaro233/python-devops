import re

with open("access_logs.txt") as file:
  file_read = file.read()
  
  regex = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
  ip_list =  re.findall(regex, file_read)
  print(ip_list)