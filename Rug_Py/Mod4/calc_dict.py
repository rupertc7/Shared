# Purpose: calcs the sum of all items in a dictionary
# How:     Syntactic Sugar experiments
# Status:  it works
# Elements: for, index, range, enumerate, Walrus operator
# Imports: num2words
# Author: ROC
# Date: 2023-11-10
# Note: 
#______________________________________________________________________

# use enumerate when you need both the index and the value, and use a simple loop or comprehension when you only need the index or the value.
dict1 = {x: x + y for x, y in enumerate(range (10))} 
print('dict1 = ' + str(dict1))

# not need to enumerate this as the index is iterated one at a time
dict2 = {index: 5 * index for index in range(10)}
print('dict2 = ' + str(dict2))

# import external module
from num2words import num2words

# Got this wrong, it changes the value not the index. 
dict3v1 = {index: num2words(index) for index in dict2}
print('dict3v1 = ' + str(dict3v1) + ' NOT intended output')
dict3v2 = {num2words(index): index for index in dict2}  #the first thing you write in a comprehension is an expression. Everything else will follow the expression's syntax
print('dict3v2 = ' + str(dict3v2) + ' intended output')


# fixed error
dict4 = {num2words(index): value for index, value in dict2.items()}
print('dict4 = ' + str(dict4))

# take the k, v in dict2 and change the k to words
dict5 = {num2words(k): v for k, v in dict2.items()}
print('dict5 = ' + str(dict5))

# Sum the values of the dictionary dict 4
total = sum(v for k, v in dict4.items())
print('Sum of dict4 = ' + str(total))

# Using SUM and Print combined the values of the dictionary dict 4
print('Sum of dict4 in a print statement = ' + str(sum(dict4.values())))

# using the walrus operator :=  The walrus operator allows 
# you to assign a value to a variable as part of an expression. 
# Read lines from a file until a line contains 'stop'
# with open('example.txt', 'r') as file:
#     while (line := file.readline().strip()) != 'stop':
#         print(line)
total = 0
[total := total + v for v in dict4.values()]
print('Using walrus operator the Sum of dict4 = ' + str(total))
