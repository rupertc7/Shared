import logging
from num2words import num2words

# Configure the logging module to write to a file
logging.basicConfig(filename='log_perimeter.log', level=logging.DEBUG)

# Function to get the shape and the number of sides
def get_shape_and_sides():
    shape = input("\nPlease state the name of the shape for which the perimeter is to be calculated: ")
    shapes = {"t": 3, "circle": 1, "open angle": 2, "triangle": 3, "square": 4, "rectangle": 4, "diamond": 4, "rhombus": 4, "pentagon": 5, "hexagon": 6, "heptagon": 7, "octagon": 8, "nonagon": 9, "decagon": 10, "hendecagon": 11, "dodecagon": 12, "tridecagon": 13, "tetradecagon": 14, "pentadecagon": 15, "hexadecagon": 16, "heptadecagon": 17, "octadecagon": 18, "enneadecagon": 19, "icosagon": 20, "triacontagon": 30, "tetracontagon": 40, "pentacontagon": 50, "hexacontagon": 60, "heptacontagon": 70, "octacontagon": 80, "enneacontagon": 90, "centagon": 100, "chiliagon": 1000}
    
    try:
        num_sides = shapes[shape]
    except KeyError:
        print("\nSHAPE NOT RECOGNIZED\nPlease check your spelling and try again.")
        logging.warning("Shape not recognized, text entered: " + str(shape))
        exit()
    
    return shape, num_sides

# Function to get the units
def get_units():
    units = input("\nPlease state the measurement units: ")
    return units

# Function to get side lengths
def get_side_lengths(num_sides):
    side_lengths = []
    for i in range(num_sides):
        side_length = int(input("\nEnter length of side {}: ".format(i+1)))
        side_lengths.append(side_length)
    return side_lengths

# Function to calculate the perimeter
def calculate_perimeter(shape, side_lengths):
    perimeter = sum(side_lengths)
    return shape, perimeter

# Function to print the results
def print_results(shape, side_lengths, units, perimeter):
    perimeter_formatted = "{:,}".format(perimeter)
    perimeter_words = num2words(int(perimeter)).replace('-', ' ')
    print(f"\n\tThe perimeter of the specified {shape}\n\twith sides of: {side_lengths} {units}\n\tPerimeter of: {perimeter_words}: {perimeter_formatted} {units}\n\n")

def main():
    shape, num_sides = get_shape_and_sides()
    units = get_units()

    if shape.lower() == "square":
        num_sides = 4
        side_length = int(input("\nEnter the length of one side: "))
        side_lengths = [side_length] * num_sides
    else:
        regular = input(f"\nPlease state if the {shape} is REGULAR (Y/N) ")
        if regular.lower() == "y":
            side_length = int(input("\nEnter the length of one side: "))
            side_lengths = [side_length] * num_sides
        else:
            side_lengths = get_side_lengths(num_sides)

    shape, perimeter = calculate_perimeter(shape, side_lengths)
    print_results(shape, side_lengths, units, perimeter)

if __name__ == "__main__":
    main()
