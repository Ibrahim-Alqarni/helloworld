"""
P10: Writing Regex's
Author: Ibrahim Alqarni
Python version 3.8.1
"""
import re
import os

file_name = input("Enter the file name: ")

def regex(file):
    "Extract the number from each of the lines then cmpute avg of numbers and print numbers of lines"
    try:
        fl= open(file, 'r')
    except FileNotFoundError:
        print("file not found") 
    else:
        filesize = os.path.getsize(file)

        if filesize == 0:
            print ("The file is empty")
            return

        with fl:
            lines= fl.read()
        linematch = re.findall(r'New Revision: ([0-9]\.d+|\d+)',lines)
        num = [float(re.search('\d+',s).group()) for s in linematch]

        if len(num)>0:
            print(" The avgerage = ", str(round(sum(num)/len(num),1)))
            print(" The number of lines = ", len(num))           
        else:
            print("No matching line found ")

regex(file_name)
