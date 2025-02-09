#! /usr/bin/python3
# source_path = "/Users/waseem/Developer/python-lab/Hello.py"
# destination_path = "/Users/waseem/Developer/python-lab/myTest/newHello.py"
source_path = input("Enter source path with filename : ")
destination_path = input("Enter destination path with filename : ")

open_source_file = open(source_path, 'r')
read_source_content = open_source_file.read()
open_source_file.close()
print("***** Printing file contents start here *****")
print(read_source_content)
print("***** Printing file contents end here *****")

open_dest_file = open(destination_path, 'w')
write_dest_file = open_dest_file.write(read_source_content)
print("Content Copied Successfuly!!!")
open_dest_file.close()
