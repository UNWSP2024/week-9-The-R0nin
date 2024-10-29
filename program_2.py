# Program #2: Random Number File Writer
# Write a program that writes a series of random numbers (up to 1000) to a file.
# Each random number should be in the range of 1 through 500. 
# The application should let the user specify how many random numbers the file will hold 
# (up to 1000).
import random
amount = 0
rounds = int(input('number of rounds: '))
with open('number.txt', 'w'):
    while amount < rounds and rounds <= 1000:
        with open('number.txt', 'a') as f:  
            number = random.randint(0, 500)
            lines = str(number) + '\n'
            f.writelines(str(lines))        
            amount = amount + 1
