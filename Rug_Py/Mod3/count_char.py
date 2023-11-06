# Purpose:      counts char, int, and symbols, 2 solutions
# How:             
# Status:       it works  
# Elements:     isdigit, isalph, not isalnum
# Imports:      
# Author:       ROC
# Date:         6/11/23
# Note:         sol 2 not mine, for ref
#______________________________________________________________________

# ROC 3/11/2023 homework week 3
# Count letters, digit and special symbols:
# Write a program that count all letters, digits and special symbols from a given string:
# Input:
# 	'P@#yn26at^&i5ve'
# Output:
# 	Chars = 8
# 	Digits = 3
# 	Symbol = 4

# set variables
int_count = 0
char_count = 0
symb_count = 0

data = 'P@#yn26at^&i5ve'
for char in data:
    if char.isdigit():
        int_count += 1
    elif char.isalpha():
        char_count +=1
    else:
        symb_count +=1

print(f'''
\t\t\tSolution 1      

\t\t\tdigits \t\t= {int_count}
\t\t\tcharacters \t= {char_count}
\t\t\tsymbols \t= {symb_count}
''')

# Solution 2

char_count1 = sum(1 for char in data if char.isalpha())
int_count1 = sum(1 for char in data if char.isdigit())
symbol_count1 = sum(1 for char in data if not char.isalnum())
print(f'''
\t\t\tSolution 2   

\t\t\tCharacter count:= {char_count1}
\t\t\tInteger count:  = {int_count1}
\t\t\tSymbol count:   = {symbol_count1}
''')


