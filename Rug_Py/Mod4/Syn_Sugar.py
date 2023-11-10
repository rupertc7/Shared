# Purpose: Examples and learning Syntactic sugar Vs alternate coding
# How: trial and error, research
# Status: In progress
# Elements: 
# Imports: 
# Author: ROC
# Date: 2023-11-10
# Note: 
#______________________________________________________________________

# eg 1
# Without syntactic sugar
squared_numbers = []
for num in range(5):
    squared_numbers.append(num ** 2)
print(squared_numbers)

# With syntactic sugar (list comprehension)
squared_numbers1 = [num ** 2 for num in range(5)]
print(squared_numbers1)

