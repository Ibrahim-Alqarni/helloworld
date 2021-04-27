"""
P8: Counting unique items: The script print the sender name 
    and count the number of times the sender sent an email
Author: Ibrahim Alqarni
Date: 03/30/2020 
Python version 3.8.1
version: 1.0
"""

import os

file_name = input("Enter the file name: ")

def count_item(file):
    'print sender email and the number of times he sent an email'

    emails = []
    d = dict()

    try:
        fl = open(file, 'r')

    except FileNotFoundError:
        print ("file name not found")
    except OSError:
        print("file is not exist")
    
    else:
        filesize = os.path.getsize(file)
        if filesize == 0:
            print ("The file is empty")

        with fl:
            for line in fl:
                line.strip("\n")
                if line.startswith("From:") and line.find("@")>0:
                    emails.append(line.split()[1])
                else:
                    continue

            for i in emails:
                d[i] = d.get(i,0) + 1
            if not d:
                'if the file has no From: '
                print("There is no sender email in this file")
            else:
                print(max(d.items()))          

count_item(file_name)