# by Kami Bigdely
# PEP8 - whitespaces and variable names.
# This is a guess game. Guess what number the computer has chosen!
import random
lowerLimit = 0
upperLimit = 100
randomNumber = random.randint(lowerLimit, upperLimit)
print('The computer has selected a number between 0 and 100. \
    Use your supernatural superpowers to guess what the number is.')
while True:
    userGuess = int(input("Enter a number between 0 and 100 (including): "))
    if userGuess > randomNumber:
        print("Guess a smaller number.")
    elif userGuess < randomNumber:
        print("Guess a larger number.")
    else:  # userGuess == randomNumber:
        print("You Won!")
        break
