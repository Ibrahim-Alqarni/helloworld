"""
P7: Finding unique strings
Author: Ibrahim Alqarni
Date: 03/17/2020 
Python version 3.8.1
version: 1.0
"""

import os

def unique_string(file):
    emails = set()
    try:
        read_file= open(file,"r")

    except FileNotFoundError:
            print ("File name not found", file)

    except NameError:
            print("File name cannont oppend",file)
    
    else:
            filesize = os.path.getsize(file)
            if filesize == 0:
                    print ("The file is empty")
            for line in read_file:
                line.strip("\n")
                if line.startswith("From:") and line.find("@")>0:
                    emails.add(line[6:])  
                else: 
                    continue
            if len(emails) == 0:
                return print("There is no emails in the file")  
                         
            print("The number of unique emails is: ", len(emails))

file_name = input("Enter the file name: ")
unique_string(file_name)