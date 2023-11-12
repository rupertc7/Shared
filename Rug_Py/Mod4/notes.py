# Purpose: NOTE TAKING
# How: 
# Status:  screen shots to transcribe
# Elements: 
# Imports: 
# Author:  ROC
# Date:    2023-11-09
# Note: 
#______________________________________________________________________

# test =  'hello'
# test[1] = 3     # this fails as the string is immutable

# letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# print(set(letters))   # set is not ordered and the order changes.

# python allows nesting of different types of data types / structures.
# if something can be accessed by indexing then it is sequenced.
# list [...]   dictionary { ... }    Tuple  ( ... )    set { ... }
#  ordered      ordered               ordered         unordered
#  mutable      mutable               immutabe        mutable
#  allows dups  unique key           allows dups      no duplicated

# Lists are general purpose, not preformace based,  sequential, use indexs
# dictionaries: are key value pairs,  i.e. pull two lists together. map data together. retrieval faster. 
# tuple is very similar to list, but immutable. stops accidentally changes the data. 
# set are used to remove duplicates. ideal for finding what is in common and not.

# Lists
# cars = ['Ford', 'BMW', 'Volvo', 'ford']
# cars.sort()
# print(cars)

# test = 'hello'
# print(list(test))

# test2 = ['test', 'apple', '[1,2,3]']
# # print(list(test2))
# # print(cars.count('ford'))
# # print(cars.index('BMW'))
# # print(cars.reverse())
# # cars.append('Aston')
# # cars.pop()
# # cars.sort()
# # popped_item =  cars.pop()
# # print(popped_item)

# lst = [1,2,3,4,5,6,7,8,9,10]
# # new_list=[]

# # for num in lst:
# #     if num != 5:
# #         new_list.append(num)

# # print(new_list)

# # syntactic sugar
# new_list = [num for num in lst if num !=5]
# print(new_list)

# # syntactic sugar
# new_list = [num for num in range(10)]
# print(new_list)

# print(lst[2])
# print(lst[:3])

# my_dict = {}
# print(dict([('eggs',2), ('bacon', 1), ('milk', 4)]))

sups ={'Batman':[1, 2, 3, 4, 5, 6],
       'Superman': {'a': ['hello', 'bye'], 'b': 2, 'c': 3, 'e': 4},
       'Spiderman': 'Peter Parker'}

print(sups['Superman']['a'][0])
print(sups['Superman']['a'][1])
print(sups['Superman']['a'][1])

# print(sups.get('ironman'])) # returns a "none" rather than giving an error. 

# sups = {'batman': 'bruce wayne', 'superman': 'clark kent', 'spiderman': 'peter parker' }

# print(sups.keys())
# print(sups.values())
# print(sups.items())

# print(sups.get('ironman')) #  get returns none rather than giving an error. 
# print(sups.get('ironman', 'tony stark')) #  this get says try ironman if not then try tony stark 


# for names in sups.values():
#     print(names)

# for k, v in sups.items():
#     print(f'{k} - {v}')


# keys = ['a','b','c','e']
# values =  [1,2,3,4]

# new_dict = {k:v for (k,v) in zip(keys, values)} # zip pulls the two lists together to create a new dict
# print(new_dict)

# my_list = ['a','b','c','e']
# new_dict = {x:x.upper() for x in my_list}
# print(new_dict)

# # sups = {'batman': ['a','b','c','e'], 'superman': 'clark kent', 'spiderman': 'peter parker' }


# t =  12345, 543231, 'hello'
# t = ()
# print(t[0])

# my_set = {1,1,2,3,4,5,6}
# # print(my_set)

# person = {'name':'Sam', 'age': 42}
# name, age = person['name'], person['age']

# # I can write this
# person = ('Sam', 42)
# name, age = person

# # Sytactic Sugar
# new_list = [num for num in my_set if num != 5]
# print(new_list)
