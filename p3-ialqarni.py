""" P3: User defined functions --> Finding the max value among the three values 
    Author: Ibrahim Alqarni
    Date: 02/14/2020 
    Python version 3.8.1
    version 2
"""

def maxOfThree(first, second, third):     
# The rules for finding the maximum number 

    if first >= second and first >= third:
        maximum = first
    elif second >= first and second >= third :
        maximum = second
    else:
        maximum = third
    print(f"The maximum number of {first}, {second}, {third} is ---> {maximum}")


def get_number(prompt: str) -> float:
    """ read and return a number from the user.                                        
        Loop until the user provides a valid number.
    """                                                                                  
    while True:
        inp: str = input(prompt)
        try:
            return float(inp)
        except ValueError:
            print(f"Error: '{inp}' is not a number. Please try again...")

def main() -> None:
    first = get_number("Enter the first number: ") 
    second = get_number("Enter the second number: ")
    third = get_number("Enter the third number: ")
    
    maxOfThree(first, second, third)  

if __name__ == "__main__":                
    main()


"""    
while True:
    inp: str = input(prompt)
    try:
        int_imp = int(inp)
        if int_imp >= 1 and int_imp <= 20:
            return int_imp
        print("Error: input must be an integer between 1 and 20")
    except ValueError:
        print(f"Error: '{inp}' is not a number. Please try again...")
"""

"""    
while True:

    inp: str = input(prompt)

    try:
        num = float(inp)
        if num < 1 or num > 20:
            raise Exception
        return num

    except ValueError:
        print(f"Error: '{inp}' is not a number. Please try again...")
    except:
        print('The entered number is not in range [1-20]')
"""