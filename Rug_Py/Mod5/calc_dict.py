# Purpose: calcs the sum of all items in a dictionary
# How:     Syntactic Sugar experiments
# Status:  FAIL cannot find the error yet.
# Elements: for, index, range, enumerate, Walrus operator
# Imports: num2words
# Author:  ROC
# Date:    2023-11-19
# Note: 
#______________________________________________________________________

# # use enumerate when you need both the index and the value, and use a simple loop or comprehension when you only need the index or the value.
# dict1 = {x: x + y for x, y in enumerate(range (10))} 
# print('dict1 = ' + str(dict1))

def dict_1():
    dict1 = {x: x + y for x, y in enumerate(range (10))} 
    print('dict1 = ' + str(dict1))

# # not need to enumerate this as the index is iterated one at a time
# dict2 = {index: 5 * index for index in range(10)}
# print('dict2 = ' + str(dict2))

def dict_2():
    # global dict2
    #dict2 = {index: 5 * index for index in range(10)}
    return {index: 5 * index for index in range(10)}
    #print('dict2 = ' + str(dict2))


# import external module
from num2words import num2words

# # Got this wrong, it changes the value not the index. 
# dict3v1 = {index: num2words(index) for index in dict2}
# print('dict3v1 = ' + str(dict3v1) + ' NOT intended output')
# dict3v2 = {num2words(index): index for index in dict2}  #the first thing you write in a comprehension is an expression. Everything else will follow the expression's syntax
# print('dict3v2 = ' + str(dict3v2) + ' intended output')

def dict_3():
    dict2 = dict_2()
    dict3v1 = {index: num2words(index) for index in dict2}
    print('dict3v1 = ' + str(dict3v1) + ' NOT intended output')
    dict3v2 = {num2words(index): index for index in dict2}  #the first thing you write in a comprehension is an expression. Everything else will follow the expression's syntax
    print('dict3v2 = ' + str(dict3v2) + ' intended output')


# fixed error
# dict4 = {num2words(index): value for index, value in dict2.items()}
# print('dict4 = ' + str(dict4))

# def dict_4():
#     dict4 = {num2words(index): value for index, value in dict2.items()}
#     print('dict4 = ' + str(dict4))

def dict_4(dict2):
    dict4 = {num2words(index): value for index, value in dict2.items()}
    print('dict4 = ' + str(dict4))
    return dict4


# # take the k, v in dict2 and change the k to words
# dict5 = {num2words(k): v for k, v in dict2.items()}
# print('dict5 = ' + str(dict5))

def dict_5():
    dict2 = dict_2()
    dict5 = {num2words(k): v for k, v in dict2.items()}
    print('dict5 = ' + str(dict5))


# # Sum the values of the dictionary dict 4
# # total = sum(v for k, v in dict4.items())
# # print('Sum of dict4 = ' + str(total))

# # Using SUM and Print combined the values of the dictionary dict 4
# print('Sum of dict4 in a print statement = ' + str(sum(dict4.values())))

def total_a():
    total = sum(v for k, v in dict4.items())
    print('Sum of dict4 = ' + str(total))
    print('Sum of dict4 in a print statement = ' + str(sum(dict4.values())))




# using the walrus operator :=  The walrus operator allows 
# you to assign a value to a variable as part of an expression. 
# Read lines from a file until a line contains 'stop'
# with open('example.txt', 'r') as file:
#     while (line := file.readline().strip()) != 'stop':
#         print(line)
# total = 0
# [total := total + v for v in dict4.values()]
# print('Using walrus operator the Sum of dict4 = ' + str(total))

def total_b(dict4):
    total = 0
    [total := total + v for v in dict4.values()]
    print('Using walrus operator the Sum of dict4 = ' + str(total))


# def main():
#     dict_1()
#     dict_2()
#     dict_3()
#     dict_4()
#     dict_5()
#     total_a()
#     total_b()

def main():
    dict_1()
    dict2 = dict_2()
    dict_3()
    dict4 = dict_4(dict2)
    dict_5()
    total_a(dict4)
    total_b(dict4)


if __name__ == "__main__":   # when I did not use the if __name__ fn and just used main() this code ran.   However, after its insertion, the dict2 fn was not defined
    main()

# The problem is that dict2 is defined within the dict_2() function and is not accessible in the globally or is not being passed directly to dict_4, 
# so the global fn has been added to dict2 or you have to pass dict2 to dict_4. I tried the former which did not work, now I'll try the latter. 

if __name__ == "__main__":
    # Call dict_2() and store the result in dict2
    dict2 = dict_2()
    
    # Assign the result of dict_4(dict2) to dict4
    dict4 = dict_4(dict2)
    
    # Continue with the rest of the program
    main()
