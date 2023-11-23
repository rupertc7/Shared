# Purpose:  Calculates the BMI of a person
# How:      basic math
# Status:   it works
# Elements: f string,  validation of input
# Imports: 
# Author:   ROC
# Date:     2023-11-23
# Note:     bmi = kg/height in m**2
#______________________________________________________________________

# ==============================  #######  ###   ##
# Function Definitions            #####    ## ## ##
# ==============================  ##       ##   ###

def input_word(prompt):                               # take and validate input from user
    while True:
        try:
            user_input = input(prompt)
            #if user_input.isdigit():                                                   # check it is a number
            #if user_input.replace('.', '').isdigit():                                  # Check if it's a valid float
            if user_input.replace('.', '').isdigit() and user_input.count('.') <= 1:    # replace takes out the decimals to allow isdigit to checkt the number. the count checks there is only one decimal point. 
                return float(user_input)                                                # cast to float
            else:
                print('Invalid input. Please try again.')

        except Exception as e:
            print(f'Error: {e}. Please try again.')
        
def bmi(weight, height):
    result = (weight / (height ** 2))
    print(f"Your BMI = {result:.2f}")
    
def loose(weight, height):    
    min_value = weight - (24.5 * (height **2))                                          # min and max are built in fns so cannot use them as fn names
    max_value = weight - (20.5 * (height **2))
    print(f"You need to loose between = {min_value:.2f} and {max_value:.2f} Kg")
    return min_value, max_value
    
def calculate_target_weight(weight, height, min_value, max_value):
    target_min = weight - min_value
    target_max = weight - max_value
    print(f'You should aim to weigh between {target_min:.1f} and {target_max:.1f} Kg')

# ==============================  ###     ###     ##     ##  ###   ##
# Main function                   ## ## ## ##   ##  ##   ##  ## ## ##
# ==============================  ##  ###  ##  ##    ##  ##  ##   ###
def main():
    weight = input_word('Please enter your weight in Kg: ')
    height = input_word("Please input your height in meters: ")
    
    bmi(weight, height)
    min_value, max_value = loose(weight, height)                                          # need this to pass the args to the next fn
    calculate_target_weight(weight, height, min_value, max_value)
    
if __name__ == '__main__':
    main()