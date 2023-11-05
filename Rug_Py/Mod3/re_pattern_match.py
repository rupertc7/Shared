# Purpose:     remove blank space in text: 2 solutions
# How:         split on space, and pattern matching
# Status:      in prog
# Elements:   split, for,  &  re
# Imports:     re
# Author:       ROC
# Date:       2/11/23    
# Note:       was fully working when it was lost. 
#______________________________________________________________________

# ROC 2/11/2023  Homework week 3
# Remove extra spaces between words:
# Given the following sentence, find a way to remove all the extra spaces and print the same sentence with just one space between words.

# paragraph = "Argentina  wins   football   world cup 2022 in a nail biting final match that led to a       spectacular    penalty shootout. Football lovers   across the world   hailed   it as one of the most    memorable   matches."

# Sol 1.  split on white spaces, then print without a loop cutting off the \n in the print

para = 'Argentina  wins   football   world cup 2022 in a nail biting final match that led to a       spectacular    penalty shootout. Football lovers   across the world   hailed   it as one of the most    memorable   matches.'
output = para.split()  # creats a list of the words
for entry in output:
    print(entry, end=' ') # prints the first word, then loops cutting off the \n and replacing with a space.
