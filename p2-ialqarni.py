
"""
    P2: Convert numeric scores to grades
    Author: Ibrahim Alqarni
    Date: 02/11/2020 
    Python version 3.8.1
    version 2 
"""

input_score= input("Please enter quiz score: ")

try:
    """convert the input to a float"""
    score= float(input_score)
# Handling the invalid inputs if the input is not a Number         
except ValueError:
    print (f"This is not a number ({input_score})")
#    raise SystemExit 
else: 



    """ 
        The rules of the letters with the grades as follows: 
    """
#    if score < 101 and score >= 93:
    if 93 <= score <= 100:         # better way to write it   
        print("A")
    elif score < 93 and score >= 90:
        print("A-")                       
    elif score < 90 and score >= 87:
        print("B+")     
    elif score < 87 and score >= 83:
        print("B")    
    elif score < 83 and score >= 80:
        print("B-")  
    elif score < 80 and score >= 70:
        print("C")  
    elif score < 70 and score >= 0:
        print("F") 
    # Handling the invalid inputs if the input more than 100 or less than 0 
    else:                    
        print ("The score should be between 0 --> 100")