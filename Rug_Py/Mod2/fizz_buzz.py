# ROC 27/10/2023  Homework 2
# Write a program that, given a number, it will play the fizz buzz game
# Hint: check again what the modulo operator does
# Hint: check for loops and the range() function

try:
    input_number = int(input("Enter a number: "))
except ValueError:
    print("You must enter a valid number")

if input_number % 3 == 0 and input_number % 5 == 0:
    print('FizzBuzz')
elif input_number % 3 == 0:
    print('Fizz')
elif input_number % 5 == 0:
    print('Buzz')
else:
    print('Please play again!')
