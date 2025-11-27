#A game to guess the target number

import random

target_number = random.randint(1, 100)

print("Welcome to 'Guess the Number' game!")
print("I have selected a number between 1 and 100. Can you guess it?")
print(" Target number for testing purposes:", target_number)  # For testing purposes; remove in production

while True:

    user_input = input("Enter number between 1 to 100 to guess the target number or Press Q to EXIT: ")
    
    if user_input.lower() == 'q':
        print("Thanks for playing! Goodbye.")
        break

    user_input = int(user_input)

    if user_input == target_number:
        print("Congratulations! You've guessed the correct number!")
        print("----Game Over----")
        break
    elif user_input < target_number:
        print("Your guess is too low. Try again.")
    else:
        print("Your guess is too high. Try again.")