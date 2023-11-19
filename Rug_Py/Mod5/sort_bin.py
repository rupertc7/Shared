# Purpose:  sorts list of binary returning an index
# How: 
# Status:  RE-WRITE
# Elements: 
# Imports:  from operator import index     import random
# Author:   ROC
# Date:     2023-11-10
#
# Note: Create a program based on the binary search algorithm.
# The program should take a list as the number to be found in such list as inputs and returns the index with the position of such number in the (sorted) list.
# Ex			lst = [0, 34, 56, 2, 4, 9, 78]
# 			    num = 56
# Output:
# 		        “The number 56 is included in the list in position 5”
#______________________________________________________________________
# Plan
#========================================================================
# import random
# create a list populated with 50, 2 digit random numbers between 10 and 99 inclusive
# print the list, sort the list
# on input of a number by an external user, print out its index in the form
# “The number 56 is included in the list in position 5”
# or confirm its not in the list.
#______________________________________________________________________

# import external module
from operator import index
import random
# create a list populated with 50, 2 digit random numbers between 10 and 99 inclusive, and print lst
lst = sorted(random.sample(range(10, 100), 50))
print(lst)

# take user input, validate or exit
query = input('Please enter the number that you wish to confirm is in the list, or type X to exit: ')
if query.lower() == 'x':
    print('\t\tYou have exited the function!')
    exit()
elif not (10 <= int(query) <= 99):
    print('Number not in lst or out or range: 10 to 99 inclusive. ')
else:
    try:
        index = lst.index(int(query))
        print("The number " + query + " is included in the list in position " + str(index))
    except ValueError:
        print("The number " + query + " is not in the list.")