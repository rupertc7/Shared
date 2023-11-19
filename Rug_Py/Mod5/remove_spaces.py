# Purpose:     remove blank space in text: 2 solutions
# How:         split on space, substitue using pattern matching
# Status:  RE-WRITE
# Elements:    split, for,  &  re.sub
# Imports:     re
# Author:      ROC
# Date:        2/11/23    
# Note:        was fully working when it was lost. 
#______________________________________________________________________

# ROC 2/11/2023  Homework week 3
# Remove extra spaces between words:
# Given the following sentence, find a way to remove all the extra spaces and print the same sentence with just one space between words.

# paragraph = "Argentina  wins   football   world cup 2022 in a nail biting final match that led to a       spectacular    penalty shootout. Football lovers   across the world   hailed   it as one of the most    memorable   matches."

# Sol 1.  split on white spaces, then print without a loop cutting off the \n in the print
print('\n\tSol 1. This simply uses split and prints only the non null entries with a space between them.')
# Sol 2.  Uses regualar expressions to achieve the same output
print('''
        Sol 2.  Uses regular expression to find and substitute the spaces.
                In this case the spaces are subbed with "-" to differentiate the solutions.\n\n''')


para = 'Argentina  wins   football   world cup 2022 in a nail biting final match that led to a       spectacular    penalty shootout. Football lovers   across the world   hailed   it as one of the most    memorable   matches.'
output = para.split()  # creats a list of the words

# print output
print('source text:-')
print(para)
print()
print('''processed text:-
      ''')
for entry in output:
    print(entry, end=' ') # prints the first word, then loops cutting off the \n and replacing with a space.
print()
print()

# Sol 2.  Uses regualar expressions to achieve the same output
# import
import re

# using para from solution 1
formated_para = re.sub(r'\s+', '-', para)
print(formated_para)
print()
print()

