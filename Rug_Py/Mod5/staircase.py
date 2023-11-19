# Purpose:     build a staircase with numbers
# How:         input steps, loops
# Status:  RE-WRITE
# Elements:    for, range
# Imports:      
# Author:      ROC
# Date:        3/11/2023
# Note:        lost
#______________________________________________________________________

# MOD 3 Homework
# Print a staircase:
# Write a script that given an integer, print a staircase made of number as shown below:
# Given the number 7:
1
22
333
4444
55555
666666
7777777
# Hint: can you nest for loops?

print('\tThis program will print a staircase of numbers')
steps = input('\tPlease input the number of steps:- ')

for i in range(1, int(steps) + 1):
    print(str(i) * (i))     # cNOTE this is a test - ignore.
