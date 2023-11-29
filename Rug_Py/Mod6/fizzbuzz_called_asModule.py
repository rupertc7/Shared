# Purpose:      calling a class
# How: 
# Status:       it works
# Elements: 
# Imports: 
# Author:       ROC
# Date:         2023-11-23
# Note:         Fizzbuzz_class_ReFactored.py

#______________________________________________________________________

import sys
sys.path.append('.')

from Fizzbuzz_class_ReFactored import FizzBuzz, get_user_input

def run_fizzbuzz():
    user_input = get_user_input()
    fizz_buzz = FizzBuzz(user_input)
    fizz_buzz.fizz_logic()

if __name__ == '__main__':
    run_fizzbuzz()
