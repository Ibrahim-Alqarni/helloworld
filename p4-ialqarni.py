"""
P4: Guess a Number using loops and a function
Author: Ibrahim Alqarni
Python version 3.8.1
"""

from random import randint

def guess_game(num_guess:int, rand_guess:int ,name: str,count:int):     
    """ The rules for finding the random number 
    """    
    if num_guess < rand_guess:
        print("Low")
        return False

    elif num_guess > rand_guess:
        print("High")
        return False

    elif num_guess == rand_guess:
        print(f"Good job, {name}! You guessed my number in {count} guesses")
        return True




    while True:
        inp: str = input(prompt)
        try:
            int_imp = int(inp)
        except ValueError:
            print(f"Error: '{inp}' is not a number. Please try again...")
        else: 
            if 1 <= int_imp <= 20:
                return int_imp
            print("Error: input must be an integer between 1 and 20")


def main() -> None:
    name: str = input("Pleas enter your name: ")
    print (f"Well, {name}, I am thinking of a number between 1 and 20.")
    rand_guess: int = randint(1, 20)

    """ the loop for limit the user try to 6 tries only
    """
    count: int = 0
    while True:
        num_guess: int = get_number("Give me your Guess: ")
        count += 1
        if guess_game(num_guess, rand_guess,name,count):
            return 
        elif count == 6:
            print(f"The number I was thinking of was {rand_guess}")
            return 
    
    for count in range(6):
        num_guess: int = get_number("Give me your Guess: ")
        if guess_game(num_guess, rand_guess,name,count):
            return 
    print(f"The number I was thinking of was {rand_guess}")
    
    
if __name__ == "__main__":                
    main()
