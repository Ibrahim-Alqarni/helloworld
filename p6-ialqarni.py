import os

def reading_file(file):
    counter = 0
    total = 0
    filesize = os.path.getsize(file)

    if filesize == 0:
        print("The file is empty")

    else:
        try:
            read_file= open(file,"r")
        except FileNotFoundError:
            print ("File name not found", file)
        except NameError:
            print("File name cannont oppend",file)

        else:
            try:
                for line in read_file:
                    line.strip("\n")
                    if not line.startswith("X-DSPAM-Confidence:"):
                        continue
                        
                    else:
                        counter+=1
                        num = float(line[21:])
                        total = num + total
                        
                avrg = str(round(total/counter,4))
                print("Average spam confidence: ", avrg)
                
            except ValueError:
                print("The file has invalid content")
                
file_name = input("Enter the file name: ")
reading_file(file_name)
