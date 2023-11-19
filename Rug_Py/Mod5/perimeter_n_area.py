# Purpose:     calc perimeter and area of shape
# How:         input steps, loops
# Status:  RE-WRITE
# Elements:    for, range
# Imports:      
# Author:      ROC
# Date:        3/11/2023
# Note:        
#______________________________________________________________________
# Rupe C 21/10/23 - Py Homework 1.  Create a program to calc the perimeter of a triangle. 
# Calc the preimeter length of a regular or non regular polygon

########### START PSUDOCODE ################
#Prompts the user to input the name of the shape for which the perimeter is to be calculated.
#Declares a dictionary of shapes and their corresponding number of sides.
#Set the number of sides based on the shape name and checks for spelling errors.
#Input measurement units.
#As squares are regular, the program sets the number of sides to 4 and asks for the length of one side.
#If regular, the program asks for the length of one side and sets the length of all sides to be the same.
#If not regular, the program asks for the length of each side.
#Sum the lengths of all sides.
#Format the perimeter as a number with commas and as words using the num2words library.
#Prints the perimeter of the shape in words and in numbers.
########### END PSUDOCODE ################

#import internal module
import logging
import math

# Configure the logging module to write to a file
logging.basicConfig(filename='log_perimeter.log', level=logging.DEBUG)

# import external module
from num2words import num2words

# Create a main function
def main():

    # Declaring the 'shape' variable before the try block, as otherwise the variable is confined to the try block only and cannot be used outside of it.
    shape = None

    try:
        # request an input of the shape that needs calculating
        shape = input("\n\n\tPlease state the name of the shape for which the perimeter is to be calulated: ")

        # delcare the shapes that can be calculated
        shapes = {"t": 3, "circle": 1, "open angle": 2, "triangle": 3, "square": 4, "rectangle": 4, "diamond": 4, "rhombus": 4, "pentagon": 5, "hexagon": 6, "heptagon": 7, "octagon": 8, "nonagon": 9, "decagon": 10, "hendecagon": 11, "dodecagon": 12, "tridecagon": 13, "tetradecagon": 14, "pentadecagon": 15, "hexadecagon": 16, "heptadecagon": 17, "octadecagon": 18, "enneadecagon": 19, "icosagon": 20, "triacontagon": 30, "tetracontagon": 40, "pentacontagon": 50, "hexacontagon": 60, "heptacontagon": 70, "octacontagon": 80, "enneacontagon": 90, "centagon": 100, "chiliagon": 1000}

        # Set the number of sides based on the shape name / Error check the spelling
        num_sides = shapes[shape]
    except KeyError:
        print("\n\t\tSHAPE NOT RECOGNISED\n\t\tPlease check your spelling and try again.\n\t\tErrors logged to 'log_perimeter.log'\n\n")  # on screen warning
        logging.warning("shape not recognised, text entered :- " + str(shape))      # output to a log file log_perimeter.log
        exit()

    # ask for the units
    units = input("\tPlease state the measurment's units: ")

    # Conditional - if the shape is a square it is automatically regular
    if shape.lower() == "square":
        num_sides = 4
        side_length = int(input("\n\t\tEnter the length of one side: "))
        side_lengths = [side_length] * num_sides
    else:
        # Conditional - if the shape is regular we only need to ask for one length
        regular = input("\tPlease state if the " + shape + " is REGULAR (Y/N) ")
        if regular.lower() == "y" :
            side_length = int(input("\n\t\tEnter the length of one side: "))
            side_lengths = [side_length] * num_sides
        else:
            side_lengths = []
            for i in range(num_sides):
                side_length = int(input("\n\t\tEnter length of side {}: ".format(i+1)))
                side_lengths.append(side_length)

    # calculate the perimeter
    perimeter = sum(side_lengths)
    perimeter_formatted = "{:,}".format(perimeter)
    perimeter_words = num2words(int(perimeter)).replace('-', ' ')

    # print output
    print('\n\t\tThe perimeter of the specified ' + shape + '\n\t\twith sides of: ' + str(side_lengths) + ' ' + units + '\n\t\tPerimeter of: ' + str(perimeter_words) + ': '+ str(perimeter_formatted) + ' ' + units + '\n\n')

    if regular.lower() == "y":
        area=(perimeter ** 2) / (4 * math.tan(math.pi / num_sides))
        rounded_area=round(area, 2)
        print("""
              This program cannot calc the area on non regular polygons. 
              However, this shape is regular.
              Its area = {} {}²
              """.format(rounded_area, units))
                
if __name__ == "__main__":
    main()