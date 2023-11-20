# Purpose:     palindrome check 2 solutions
# How:         word reversal, and char compare
# Status:      RE-WRITE
# Elements:    for, if
# Imports:      
# Author:       ROC
# Date:         20/11/2023 
# Note:   
#______________________________________________________________________

# ==============================
# Function Definitions
# ==============================

def input_word():                               # take and validate input from user
    while True:
        try:
            user_input = input('Enter input: ')
            if user_input.isalnum():
                return user_input               # Return the input directly
            else:
                print('Invalid input. Please try again.')
        except Exception as e:
            print(f'Error: {e}. Please try again.')

def pal(word):                                  # Solution 1 - reversal of the word
    rev = word[::-1]
    print('\nSolution 1 - word reversal technique\n')
    if word == rev:
        print(f'\tThe word "{word.upper()}" is a palindrome')
    else:
        print(f'\tThe word "{word.upper()}" is NOT a palindrome')
        
def compare(word):                              # Solution 2 - compare components of the string from opposite ends.
    print('\n\nSolution 2 - character comparison technique\n')
    right = len(word) - 1
    left = 0
    for char in word:
        if word[left] == word[right]:
            left += 1
            right -= 1
        else:
            print(f'\tThe word "{word.upper()}" is a NOT a palindrome\n')
            return                              # Return here to exit the function when a mismatch is found
    print(f'\tThe word "{word.upper()}" is a palindrome\n')

# ==============================  ###     ###     ##     ##  ###   ##
# Main function                   ## ## ## ##   ##  ##   ##  ## ## ##
# ==============================  ##  ###  ##  ##    ##  ##  ##   ### 
def main():
    word = input_word()                         # Get the input from the user and pass to the other fns
    pal(word)
    compare(word)

if __name__ == '__main__':
    main()
