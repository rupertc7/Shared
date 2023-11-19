# Purpose:     palindrome check 2 solutions
# How:         word reversal, and char compare
# Status:  RE-WRITE
# Elements:    for, if
# Imports:      
# Author:       ROC
# Date:         2/11/2023 
# Note:   
#______________________________________________________________________

# ROC 2/11/2023  write a program that checks if a word is a palindrome

# Solution 1 - reversal of the word
def pal(word):
    rev = word[::-1]
    print('\nSolution 1 - word reversal technique\n')
    if word == rev:
        print(f'\tThe word "{word.upper()}" is a palindrome')
    else:
        print(f'\tThe word "{word.upper()}" is a NOT a palindrome')

word = input('Please enter a word for checking:- ')
pal(word)

# Solution 2 - compare components of the string from opposite ends.
def compare(word):
    print('\n\nSolution 2 - character comparison technique\n')

    right = len(word) - 1
    left = 0
    for char in word:
        if word[left] == word[right]:
            left += 1
            right -= 1
        else:
            print(f'\tThe word "{word.upper()}" is a NOT a palindrome\n')
        return
    print(f'\tThe word "{word.upper()}" is a palindrome\n')

compare(word)