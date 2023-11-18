# Purpose: mod5 lesson notes
# How: practice in class
# Status: writing as we go
# Elements: 
# Imports: 
# Author: ROC
# Date: 2023-11-18
# Note: 
#______________________________________________________________________


# test = 'thisisatest'
# counter = 0
# for char in test:
#     counter += 1
# print(counter)

# test1 = 'thisisateststring'
# counter = 0
# for char in test1:
#     counter += 1
# print(counter)


# # how could I have written this as a function?

# print(len(test))


# def name of function():
#     code to execute
#     return value returned by the function

# Remember: function must be called to be executed. To call a function you just need the following syntax:

# name of the function()
# return kick you out of a function. 
# so in lambda use return to kick out of lambda to stop being charged. 


# def saying_hello():
#     print('hello')
#     return


# saying_hello()   # until this line the function is not called at all until it is called. 

# # def age_calculator(current_year, birth_year): # arguments
# #     age = int(current_year) - int(birth_year) # parameters are the values going into the arguments
# #     return age 

# # my_age = age_calculator(2023, 1963)

# def only_if_approved(approved=True):
#     if approved:
#         saying_hello()
#     else:
#         print('you are not approved')
#     return

# only_if_approved()
# # alt
# def only_if_approved(approved=True):
#     if approved:
#         return saying_hello()
#     return 'you are not approved'
    
# only_if_approved()

# lambda is top down, python tends to be bottom up. 

x=5
y=3
print(x*y)
