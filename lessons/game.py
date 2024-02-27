"""Number guessing game."""
from random import randint

SECRET: int = randint(1,10)
correct : bool = False

while correct == False: #not correct
    guess: int = int(input("Guess a number: "))
    if guess == SECRET:
        print(f" {guess} is the correct answer! " + "Great job! ")
        correct = True
    else: 
        if guess >= SECRET:
            print(f" {guess} is too high of a guess! " + "Try again! ")
        if guess <= SECRET:
            print(f" {guess} is too low of a guess! " + "Try again! ")
    
        
   
