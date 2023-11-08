# Purpose:  understand nested loops and continue
# How: 
# Status:   in testing
# Elements: join, len, range, append, continue
# Imports: 
# Author:   ROC
# Date:     2023-11-07
# Note: 
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
