import os
import sys
import datetime

req_path = input("Enter path: ")
file_age = 2
if not os.path.exists(req_path):
   print("Please enter a valid path")
   sys.exit(1)
if os.path.isfile(req_path):
   print("Please provide direvtory path")
   sys.exit(2)
# get current date
cur_date = datetime.datetime.now()
for each_file in os.listdir(req_path):
   #fetch path with filename[complete path]
   complete_path = os.path.join(req_path, each_file) 
   #check for files
   if os.path.isfile(complete_path):
      #get file create datetime
      file_create_datetime = datetime.datetime.fromtimestamp(os.path.getctime(complete_path))
      # print(complete_path, file_create_datetime)
      diff_days = (cur_date - file_create_datetime).days
      if diff_days > file_age:
         os.remove(complete_path)
         print(complete_path, diff_days)


