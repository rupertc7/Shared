# Purpose: remove duplicates from a list
# How: using set, lots of playing around
# Status: it works
# Elements: 
# Imports: 
# Author: ROC
# Date: 2023-11-10
# Note: remove dups from [5, 20, 15, 20, 25, 50, 20]
#______________________________________________________________________

lst = [5, 20, 15, 20, 25, 50, 20]

# using for loop to create list
lst2 = [num * 5 for num in range(10)]
print('list 2 = ' + str(lst2))

# adding list to create duplicates for removal exercise
lst1 = lst2 + lst2
print('list 1 = ' + str(lst1))

# using zip to join lists and create more duplicates ### FAILED it added the elements together and ignored the extra values.
list2dict = [x + y for x, y in zip(lst1, lst2)]
print('list2dict = ' + str(list2dict) + 'this fails as it adds the lists and cuts of the extra entries')

# using set to deduplicate and then putting the set into a list so the order is consistent.
set1_dedupped = set(lst1)
print('set1_dedupped = ' + str(set1_dedupped))
lst1_dedupped = sorted(list(set1_dedupped))
print('lst1_dedupped = ' + str(lst1_dedupped))

# The actual set problem - de duplicate lst
set1 = set(lst)
print('lst_dedupped = ' + str(sorted(set1)))

