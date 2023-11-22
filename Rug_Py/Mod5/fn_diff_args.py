# Purpose:  demo of no parameter, multi parameter, *args, *kwargs, fn in fn, recursion
# How: 
# Status:   in prog
# Elements: 
# Imports: 
# Author:   ROC
# Date:     2023-11-21
# Note: 
#______________________________________________________________________
    # Function that invokes another function​

    # A recursive function

# ==============================  ##   ###     ###   ####    ####   #####  ######
# Module Imports				  ##   ## ## ## ##   #####  ##  ##  ###	     ##
# ==============================  ##   ##  ###  ##   ##	     #### 	## ##	 ##


# ==============================    ####   ####   ###   ##
# Constants                       ##      ##  ##  ## ## ##
# ==============================    ####   ####   ##   ###
#global lst
lst = ['this', 'is', 'a', 'test', 'to', 'see', 'if', 'this', 'will', 'count', 'elements', 'OK']



first = "let see if this works"
second = "I'm expecting an output"
third = "of"
fourth = "True"

my_args = [0,1,2,3,4,5,6,7,8,9]

# ==============================  #######  ###   ##
# Function Definitions            #####    ## ## ##
# ==============================  ##       ##   ###

def count_elements():                                                 # With no parameter,
    count = (len(lst))
    print(count)
    return count

def extending_elements(first, second, third, fourth):                       # multiple parameters, ​
    mylist = []
    mylist.extend([first, second, third, fourth])
    print(len(mylist) == 4)
   
def how_many_args(*args):                                                   # *args
    total = 0
    for arg in (my_args):
        total += arg
    print(total)

def format_play(**kwargs):                                                  # *kwargs
    word_list = kwargs.get('word_list', [])
    while word_list:
        last_word = word_list.pop()                                         # Get the last word from the list
        if word_list:
            first_word = word_list.pop(0)                                   # Get the first word from the list
    print(f"last_word: {last_word.upper()}, first_word: {first_word.lower()}")
    
def default_vals(*args, power=2):                                           # default values and using a mutable object as default value
    total = sum(args)
    result = total ** power
    print(result)
    
def call_fn_in_fn():                                                        # Function that invokes another function​
    result = default_vals(*my_args, power=how_many_args(my_args))
    print(result)
    
# ==============================  ###     ###     ##     ##  ###   ##
# Main function                   ## ## ## ##   ##  ##   ##  ## ## ##
# ==============================  ##  ###  ##  ##    ##  ##  ##   ###
def main():
    count_elements()                                                        # With no parameter,
    extending_elements(first, second, third, fourth)                        # multiple parameters   
    how_many_args(*my_args)                                                 # *args
    format_play(word_list = lst.copy())                                     # * kwags - Pass the copied list to avoid modifying the original list
    default_vals(*my_args)                                                  # default values and using a mutable object as default value ​
    call_fn_in_fn()                                                         # Function that invokes another function​

    
if __name__ == '__main__':
    main() 