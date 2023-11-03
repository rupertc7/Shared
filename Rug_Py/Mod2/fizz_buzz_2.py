# ROC 27/10/2023  Homework 2
# Write a program that, given a number, it will play the fizz buzz game
# Hint: check again what the modulo operator does
# Hint: check for loops and the range() function
# print each failed number until the input number is reached

try:
    input_number = int(input("Enter a number: "))
except ValueError:
    print("You must enter a valid number")

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
