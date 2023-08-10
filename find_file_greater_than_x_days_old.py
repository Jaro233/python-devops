import os
import datetime

current_time = datetime.datetime.now()
max_age = 10

for dirpath, dirnames, filenames in os.walk("E:\\build"):
  for file in filenames:
    comp_path = os.path.join(dirpath, file)
    file_stat = os.stat(comp_path)
    # print(file_stat)
    file_ctime = file_stat.st_ctime
    file_creation_date = datetime.datetime.fromtimestamp(file_ctime)
    # print(file_creation_date)

    diff_in_days = (current_time - file_creation_date).days
    if diff_in_days > max_age:
      # os.remove()
      print(comp_path, diff_in_days)
