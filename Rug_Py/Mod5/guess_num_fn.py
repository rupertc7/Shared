# Purpose:     guess randomly generated numbers
# How:         input steps, loops
# Status:  RE-WRITE
# Elements:    for, range
# Imports:      
# Author:      ROC
# Date:        3/11/2023
# Note:        lost
#______________________________________________________________________
# ROC 27/10/2023  Homework 2/2
# While loop:
# Create a program to ask the user to guess the number that has been randomly generated. The user will be able
# to try continuously until it finds the correct number. The program should stop as soon as the number is found.
# At each iteration the program will tell the user if the number is too high, too low or the correct one.
# Extra:
# Implement a way to assign only 5 attempts to the user. Each iteration should show the attempt left.
# Hint: check what the random library does

# ==============================
# Module Imports
# ==============================
import random                                   # generates random numbers etc

# ==============================
# Constants
# ==============================

cardinal = {                                    # Create a dictionary with the cardinals
    1: 'first',
    2: 'second',
    3: 'third',
    4: 'fourth',
    5: 'fifth'
}

# ==============================
# Function Definitions
# ==============================

def user_input(attempt):                         # check the input is an integer
    while True:
        try:
            user_input = input('Please take your ' + cardinal[attempt] + ' guess at the number ')
            if user_input.isdigit():
                guess = int(user_input)
                return guess                    # Return the valid input
            else:
                print('Invalid input. Please try again.')
        except Exception as e:
            print(f'Error: {e}. Please try again.')

def generate_random():                          # Generate a random number between 0 and 100
    return random.randint(0, 100)

def guess_logic(guess, ran_num):                # logic of the game
    if guess == ran_num:
        print('Spot on!')
    elif guess > ran_num:
        print('Too high')
    else:
        print('Too low')
        
# ==============================
# Main function
# ==============================

def main():
    ran_num = generate_random()                    # Store the generated random number
    attempt = 1

    while attempt <= 5:                             # Loop until 5 attempts are exhausted
        guess = user_input(attempt)                 # Pass the attempt number to the user_input function
        guess_logic(guess, ran_num)
        
        if guess == ran_num:
            break                                   # Break the loop if the guess is correct
        else:
            attempt += 1                            # Increment the attempt for the next iteration

if __name__ == '__main__':
    main()


