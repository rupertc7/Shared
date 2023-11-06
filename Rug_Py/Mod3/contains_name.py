# Purpose:     finds and counts words in para
# How:         count fn on inputs
# Status:      it works   
# Elements:    input, count, upper
# Imports:      
# Author:      ROC
# Date:        3/11/2023
# Note:        if i want to format the input paste, I should look at Tkinter
#______________________________________________________________________

# ROC 3/11/2023  Mod 3 homework
# Check if a name is in a sentence:
# Write a script that, given a sentence and a word it will tell if the word is included in the sentence and how many time appears in the sentence.
# Output example
# Please insert a sentence: this is a test
# Please insert a word to search: test
# The word test is included in the sentence
# Extra: make it dynamic.

# # Take input text
print('\n\tThis program will take a section of text and count the number of time a set word appears in that text.')
para = input('\n\tPlease paste in a paragraph for analysis:- ')
word = input('\n\tPlease type in the word to be counted:-    ')

# Process and output
count = para.count(word)
print(f'\n\tThe word "{word.upper()}" occurs {count} times in the submitted paragraph.\n')

