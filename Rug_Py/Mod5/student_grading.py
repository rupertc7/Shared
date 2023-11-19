# Purpose:     grade a student according to the score obtained
# How:         input steps, loops
# Status:  RE-WRITE
# Elements:    TRY, IF ELSE
# Imports:      
# Author:      ROC
# Date:        3/11/2023
# Note:        lost
#______________________________________________________________________
# ROC 27/10/2023  Homework 2
# write a prog that will grade a student according to the score obtained.
# Score >= 90 : ‘A’    80<=score<=89: ‘B’    70<=score<=79 : ‘C’    60<=score<=69: ‘D’    score<59: ‘F’

while True:
    try:
        score = int(input("\tEnter your result in percent (0 - 100): "))
        if score < 0:
            print("\tPlease enter a valid, positive integer\n")
        elif score > 100:
            print("\tPlease enter a number between 0 and 100.\n")
        else:
            break # if the number is valid, break out of the loop
    except ValueError:
        print("Please enter a valid number in numerals")
        exit()

# if score < 0 or score > 100:
#     print("Please enter a number between 0 and 100, no negative numbers.")
if score >= 90:
    print("""
        =================================
        |\t\t\t\t|
        |\t\tA\t\t|
        |\t\t\t\t|
        =================================
        """)
elif score >= 80:
 print("""
        =================================
        |\t\t\t\t|
        |\t\tB\t\t|
        |\t\t\t\t|
        =================================
        """)
elif score >= 70:
 print("""
        =================================
        |\t\t\t\t|
        |\t\tC\t\t|
        |\t\t\t\t|
        =================================
        """)
elif score >= 60:
 print("""
        =================================
        |\t\t\t\t|
        |\t\tD\t\t|
        |\t\t\t\t|
        =================================
        """)
else:
 print("""
        =================================
        |\t\t\t\t|
        |\t\tF\t\t|
        |\t\t\t\t|
        =================================
        """)
