# Purpose: Fizzbuzz game
# How:   written as a class
# Status:  it works
# Elements: 
# Imports: 
# Author: ROC
# Date: 2023-11-23
# Note:   see fizzbuzz_called_asModule.py

#______________________________________________________________________
class FizzBuzz:
    def __init__(self, input_number):
        self.input_number = input_number

    def fizz_logic(self):
        if self.input_number is not None:
            i = 0
            while i < self.input_number:
                i += 1
                if i % 3 == 0 and i % 5 == 0:
                    print('FizzBuzz')
                elif i % 3 == 0:
                    print('Fizz')
                elif i % 5 == 0:
                    print('Buzz')
                else:
                    print(i)

def get_user_input():
    try:
        return int(input("Enter a number: "))
    except ValueError:
        print("You must enter a valid number")
        return None

def main():
    user_input = get_user_input()
    fizz_buzz = FizzBuzz(user_input)
    fizz_buzz.fizz_logic()

if __name__ == '__main__':
    main()

