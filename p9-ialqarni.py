"""
P9: Classic books 
Author: Ibrahim Alqarni
Python version 3.8.1
version: 1.0
"""
import string
import operator
import os

file_name = input("Enter the file name: ")

def classic_books(file):
    """read file and print summary (total words, Total distinct words, 
    The top 25 most frequent words and counts Character frequency from most to least"""

    clean_line = str.maketrans('', '', string.punctuation)
    words_num = 0
    dic_words = dict()
    dic_char = dict()
    lst_char = list()
    lst= list()
    lst2= list()

    try:
        fl= open(file, encoding="utf-8")
    except UnicodeEncodeError:
        print("the file has string wich is not ascii") # string is not ascii
    except FileNotFoundError:
        print("file not found")
    else:
        filesize = os.path.getsize(file)
        if filesize == 0:
            print ("The file is empty")
            return

        with fl: 
            for line in fl:
                line= line.translate(clean_line)
                line = line.lower()
                line= line.split()
                lst_char.extend(line)
                words_num += len(line) # count total words in file

                for word in line: # count total number of distinct words
                    dic_words[word] = dic_words.get(word,0) +1

            print("Total words = {:,} ".format(words_num))
            print("Total distinct words= {:,}".format(len(dic_words)))

            #get the top 25 frequent words and count 

            for key, value in list(dic_words.items()):
                lst.append((value, key))
            lst.sort(reverse=True)
            print("The top 25 most frequent words and counts:")

            for key, value in lst[:25]:
                print('{} = {:,}'.format(value,key))  

            # characters frequency

            for item in lst_char:
                for char in item.split():
                    char = char.strip()
                    for letter in char:
                        if letter in string.ascii_lowercase:
                            dic_char[letter] = dic_char.get(letter,0) +1

            for key, value in list(dic_char.items()):
                lst2.append((value, key))

            lst2.sort(reverse=True)

            print("Character frequency: ")

            for key, value in lst2:
                print('{} = {:,}'.format(value,key))  

classic_books(file_name)
