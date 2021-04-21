"""
P5: Convert singular words into plural
Author: Ibrahim Alqarni
Date: 03/02/2020 
Python version 3.8.1
version: 1.0
"""

def plural(some_sentence) -> list:
    """Convert each single word to plural"""
    words = some_sentence.split()
    vowels = ['a', 'e', 'i', 'o', 'u']
    plurals = []

    for word in words:
        if word.endswith('y'):
            if len(word) > 2 and word[-2] in vowels:
                plurals.append(word + 's')
            else:
                plurals.append(word[:-1] + 'ies')
        elif (len(word) > 2 and word.endswith(('ch', 'sh'))) or word[-1] in ('o', 's', 'x', 'z'):
            plurals.append(word + 'es')
        else:
            plurals.append(word + 's')
    return plurals

def main() -> None:
    input_sentence = input('Enter a sentence: ')
    new_sentence = ' '
    print(new_sentence.join(plural(input_sentence)))

if __name__ == '__main__': main()