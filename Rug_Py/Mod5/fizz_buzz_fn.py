# Purpose:     fizz buzz game
# How:         input steps, loops
# Status:      it works
# Elements:    for, range
# Imports:      
# Author:      ROC
# Date:        3/11/2023
# Note:        lost
#______________________________________________________________________
# ROC 27/10/2023  Homework 2
# Write a program that, given a number, it will play the fizz buzz game
# Hint: check again what the modulo operator does
# Hint: check for loops and the range() function
# print each failed number until the input number is reached

# ==============================
# Function Definitions
# ==============================
def get_input():
    try:
        return int(input("Enter a number: "))
    except ValueError:
        print("You must enter a valid number")

def fizz_logic(input_number):
    i = 0
    while i < input_number:
        i += 1
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)
            
# ==============================
# Main function
# ==============================
def main():
    input_number = get_input()
    if input_number != None:
        fizz_logic(input_number)

if __name__ == '__main__':
    main()
