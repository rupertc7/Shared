# Purpose:  password checker
# How:      while loop checks input
# Status:   WORKS
# Elements: while, if, else
# Imports:  none
# Author:   codewhisperer
# Date:     2/11/23

password = ''pyth
while password != 'python123':
    password = input("Enter password: ")
    if password == 'python123':
        print("You are logged in!")
    else:
        print("Sorry, try again.")