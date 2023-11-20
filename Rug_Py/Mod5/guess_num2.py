# Purpose:     guess randomly generated numbers
# How:         input steps, loops
# Status:      it works - but misses error capture
# Elements:    for, range
# Imports:      
# Author:      ROC
# Date:        3/20/2023
# Note:        
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
import random  # generates random numbers etc

# ==============================
# Constants
# ==============================

cardinal = {  # Create a dictionary with the cardinals
    1: 'first',
    2: 'second',
    3: 'third',
    4: 'fourth',
    5: 'fifth'
}

# ==============================
# Function Definitions
# ==============================

def generate_random():                          # Generate a random number between 0 and 100
    return random.randint(0, 100)

def guess_logic(cardinal, ran_num):             # 5 attempts higher lower guesses with hints as to how to guess
    attempt = 1
    while attempt <= 5:
        guess = int(input('Please take your ' + cardinal[attempt] + ' guess at the number '))
        if guess == ran_num:
            print('Spot on!')
            break
        elif guess > ran_num:
            print('Too high')
            attempt += 1
        else:
            print('Too low')
            attempt += 1
    print('Game over!')

# ==============================
# Main function
# ==============================

def main():
    ran_num = generate_random()                 # Store the generated random number
    guess_logic(cardinal, ran_num)

if __name__ == '__main__':
    main()
