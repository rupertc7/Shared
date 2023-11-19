# Purpose: calcs the sum of all items in a dictionary
# How:     Syntactic Sugar experiments
# Status:  it works
# Elements: for, index, range, enumerate, Walrus operator
# Imports: num2words
# Author:  ROC
# Date:    2023-11-19
# Note: 
# ______________________________________________________________________

# use enumerate when you need both the index and the value, and use a simple loop or comprehension when you only need the index or the value.
def dict_1():
    dict1 = {x: x + y for x, y in enumerate(range(10))}
    print('dict1 = ' + str(dict1))

# not need to enumerate this as the index is iterated one at a time
def dict_2():
    return {index: 5 * index for index in range(10)}

# import external module
from num2words import num2words

def dict_3():
    dict2 = dict_2()
    dict3v1 = {index: num2words(index) for index in dict2}
    print('dict3v1 = ' + str(dict3v1) + ' NOT intended output')
    dict3v2 = {num2words(index): index for index in dict2}
    print('dict3v2 = ' + str(dict3v2) + ' intended output')

def dict_4(dict2):
    dict4 = {num2words(index): value for index, value in dict2.items()}
    print('dict4 = ' + str(dict4))
    return dict4

def dict_5():
    dict2 = dict_2()
    dict5 = {num2words(k): v for k, v in dict2.items()}
    print('dict5 = ' + str(dict5))

def total_a(dict4):
    total = sum(v for k, v in dict4.items())
    print('Sum of dict4 = ' + str(total))
    print('Sum of dict4 in a print statement = ' + str(sum(dict4.values())))

def total_b(dict4):
    total = 0
    [total := total + v for v in dict4.values()]
    print('Using walrus operator the Sum of dict4 = ' + str(total))

def main():
    dict_1()
    dict2 = dict_2()
    dict_3()
    dict4 = dict_4(dict2)
    dict_5()
    total_a(dict4)
    total_b(dict4)

if __name__ == "__main__":
    # Continue with the rest of the program
    main()
