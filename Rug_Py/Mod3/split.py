# Purpose:     to learn using split
# How:         trial and error
# Status:      it works   
# Elements:    split
# Imports:      
# Author:      ROC
# Date:        2/11/2023
# Note:   
#______________________________________________________________________

# ROC 2/11/2023 homework week 3
# Write a program to split a given string on hyphens and display each substring
# Str1 = 'Emma-is-a-data-scientist'
# Output must have each sub-string on a new line

str1 = 'Emma-is-a-data-scientist'
output = str1.split('-')  # creats a list of the words
i = 0
for word in output:
    print(output[i]) # prints the first word, then increases the index
    i += 1