# Purpose:      counts char, int, and symbols, 2 solutions
# How:             
# Status:       it works
# Elements:     isdigit, isalph, not isalnum
# Imports:      
# Author:       ROC
# Date:         6/11/23
# Note:         sol 2 not mine, for ref
#______________________________________________________________________

# ==============================
# Function Definitions
# ==============================

def char_count(data):
    #char_count = 0
    return sum(1 for char in data if char.isalpha())  # Counting alphabetic characters

def int_count(data):
    #int_count = 0
    return sum(1 for char in data if char.isdigit())  # Counting numeric digits

def symb_count(data):
    #symb_count = 0
    return sum(1 for char in data if not char.isalnum())  # Counting symbols (non-alphanumeric characters)

def print_output(char_count, int_count, symb_count):
    print(f'''
    \t\t\tSolution  

    \t\t\tCharacter count:= {char_count}
    \t\t\tInteger count:  = {int_count}
    \t\t\tSymbol count:   = {symb_count}
    ''')

# ==============================
# Main function
# ==============================

def main():
    data = 'P@#yn26at^&i5ve'
    char_count_rtn = char_count(data)
    int_count_rtn = int_count(data)
    symb_count_rtn = symb_count(data)
    print_output(char_count_rtn, int_count_rtn, symb_count_rtn)

if __name__ == '__main__':
    main()
