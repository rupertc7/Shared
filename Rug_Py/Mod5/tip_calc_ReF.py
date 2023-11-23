# Purpose:  calcs the tip amount per person at a meal
# How: 
# Status:   it Works
# Elements: 
# Imports: 
# Author:   ROC
# Date:     2023-11-22
# Note:     I removed the constants with the user input data and put that directly in Main.
# Note:     I validate the tip percentage in this version
#______________________________________________________________________

# ==============================  #######  ###   ##
# Function Definitions            #####    ## ## ##
# ==============================  ##       ##   ###
def data_in(prompt, valid_values=None):                                      # take and validate input from user, uses optional second argument  see MAIN()
    while True:
        try:
            user_input = input(prompt)
            if user_input.isnumeric() and (valid_values is None or int(user_input) in valid_values):
                return int(user_input)                    # Return the input directly as integer
            else:
                print('Invalid input. Please try again.')

        except Exception as e:
            print(f'Error: {e}. Please try again.')

def data_out(cost, divided, percentage):
    result = ((cost + (cost * percentage / 100))/divided)
    print(f'Each person should pay: ${result:.2f}')      # :.2f  puts the result to two decimal places

# ==============================  ###     ###     ##     ##  ###   ##
# Main function                   ## ## ## ##   ##  ##   ##  ## ## ##
# ==============================  ##  ###  ##  ##    ##  ##  ##   ###
def main():
    valid_percentages = [10, 12, 15]
    
    cost = data_in("Welcome to the tip calculator.\nWhat's was the total bill? $ ")
    percentage = data_in("What percent tip would you like to give? 10, 12, or 15? ", valid_values=valid_percentages)   # second argument option used
    divided = data_in("How many people to split the bill? ")
    
    data_out(cost, divided, percentage)

if __name__ == '__main__':
    main()