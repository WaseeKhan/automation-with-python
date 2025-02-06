import os
import sys
import datetime
req_path = input("Enter path: ")
if not os.path.exists(req_path):
   print("Please enter a valid path")
   sys.exit(1)
if os.path.isfile(req_path):
   print("Please provide direvtory path")
   sys.exit(2)
for each_file in os.listdir(req_path):
   #fetch path with filename[complete path]
   complete_path = os.path.join(req_path, each_file) 
   #check for files
   if os.path.isfile(complete_path):
      print(complete_path, datetime.datetime.fromtimestamp(os.path.getctime(complete_path)))



