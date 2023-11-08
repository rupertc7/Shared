# Purpose:  understand nested loops and continue
# How: 
# Status:   it works
# Elements: join, len, range, append, continue, output [ ]
# Imports: 
# Author:   ROC
# Date:     2023-11-07
# Note:     from io import SringIO & import sys I could caputure the print output to a variable. 
#______________________________________________________________________

colours= ["red", "green", "blue"]

# nested loop
output = []
for col1 in range(len(colours)):
    for col2 in range(len(colours)):
        if col1 == col2:
            continue
        output.append(colours[col1] + '-' + colours[col2])

# alter last element in loop
if output:
    output[-1] = 'and ' + output[-1]

# print output
print(', '.join(output) + '.')
