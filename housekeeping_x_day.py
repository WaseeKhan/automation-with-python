import os
import sys
req_path = input("Enter path: ")
if not os.path.exists(req_path):
   print("Please enter a valid path")
   sys.exit(1)
if os.path.isfile(req_path):
   print("Please provide direvtory path")
   sys.exit(2)
for each_file in os.listdir(req_path):
   print(each_file)


