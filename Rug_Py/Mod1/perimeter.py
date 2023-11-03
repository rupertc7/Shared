# ROC Oct 23 Homework
# Calc the preimeter length of a regular or non regular polygon

#import external funtions
from num2words import num2words

# request an input of the shape that needs calculating
shape = input("\n\n\tPlease state the name of the shape for which the perimeter is to be calulated: ")
units = input("\tPlease state the measurment's units: ")

# delcare the shapes that can be calculated
shapes = {
    "t": 3, # t is shorthand for triangle, used only for testing. 
    "circle": 1,
    "open angle": 2,
    "triangle": 3,
    "square": 4,
    "rectangle": 4,
    "diamond": 4,
    "rhombus": 4,
    "pentagon": 5,
    "hexagon": 6,
    "heptagon": 7,
    "octagon": 8,
    "nonagon": 9,
    "decagon": 10,
    "hendecagon": 11,
    "dodecagon": 12,
    "tridecagon": 13,
    "tetradecagon": 14,
    "pentadecagon": 15,
    "hexadecagon": 16,
    "heptadecagon": 17,
    "octadecagon": 18,
    "enneadecagon": 19,
    "icosagon": 20,
    "triacontagon": 30,
    "tetracontagon": 40,
    "pentacontagon": 50,
    "hexacontagon": 60,
    "heptacontagon": 70,
    "octacontagon": 80,
    "enneacontagon": 90,
    "centagon": 100,
    "chiliagon": 1000
}

# Set the number of sides based on the shape name
num_sides = shapes[shape]

# request the length of the sides to be entered
side_lengths = []
for i in range(num_sides):
    side_length = int(input("\n\t\tEnter length of side {}: ".format(i+1)))
    side_lengths.append(side_length)

# calculate the perimeter
perimeter = sum(side_lengths)
perimeter_formatted = "{:,}".format(perimeter)
perimeter_words = num2words(int(perimeter)).replace('-', ' ')

# print output
#print('The perimeter of the specified ' + shape + ' with sides of: ' + str(side_lengths) + ' sum to: ' + str(perimeter_formatted))
print('\n\tThe perimeter of the specified ' + shape + '\n\twith sides of: ' + str(side_lengths) + ' ' + units + '\n\tPerimeter of: ' + str(perimeter_words) + ': '+ str(perimeter_formatted) + ' ' + units + '\n\n')