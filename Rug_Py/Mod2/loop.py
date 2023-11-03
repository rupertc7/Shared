
# using item to extract sequentially from a dictionary
fruit = ['apples','oranges','bananas']

for item in fruit:
    print(f'The best fruit now is {item}')

# using number to extract sequentially from a dictionary
numbers = [0,1,2,3,4,5,6,7,8,9,10]
for number in numbers:
    print(f'The next number is {number}')

# using range() to extract sequentially from a dictionary
for number in range(11):  #if the number had been 10 the number 10 would have been trimmed
    print(f'The next number is {number}')

#  to increment the counter by more than the default value of 1
for number in range(1,10,2):
    print(f'The next number is {number}')
