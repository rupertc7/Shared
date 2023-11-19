# Purpose:    to play Rock paper scissors
# How: 
# Status:  RE-WRITE
# Elements: 
# Imports:    random
# Author:     ROC
# Date:       2023-11-10
# Note: 
#______________________________________________________________________
# Rock paper scissors.
# Write a program that plays the game of rock, paper, scissors.
# Input example:
# 		Choose between ‘rock’, ‘paper’, ‘scissors’
# Output example:
# 		Player choice: rock
# Computer choice: paper
# Computer wins!
# Requirements:
# The program must ensure the user only insert accepted values. If a wrong value is inserted, 
# a message should be returned and the user should be asked to insert a value again.
# The computer must choose rock, paper or scissors randomly. Hint: check the random library.
#_____________________________________________________________________________

# import module to gen random items. 
import random as ran                                  # as ran is a shorthand that I can use to ref the module

# to generate random words from a list
rps = ['Rock', 'Paper', 'Scissors']                   
p = input('\n\t\tType in ' + ', '.join(rps) + ' Altenately type X to exit. ')
if p == 'X' or p == 'x':
    print('\t\tYou have exited the game!')
    exit()

# take input 
while p not in rps:
    p = input('\n\t\tInvalid entry. Type in ' + ', '.join(rps) + ' Altenately type X to exit. ')

# assign computer's choice to variables
c = ran.choice(rps)

# print player and computer's choice
print('\t\t    Player choice: ' + p)
print("\t\tComputer's choice: " + c)

# determine the winner
win = {'rock': 'scissors', 'scissor': 'paper', 'paper': 'rock'}

# Print results
if (c == p):
    result = 'Draw'
    print('\n\t\tIt was a tie!')
elif c != p and c == (win.keys()):
    print('\n\t\tSorry the computer won!')
else:
    print('\n\t\tHorah Horah you won! The computer lost. What a dood!!\n\n')

