# # Purpose: Notes for Mod6
# # How: 
# # Status: not started
# # Elements: 
# # Imports: 
# # Author: ROC
# # Date: 2023-11-23
# # Note: 
# #______________________________________________________________________

# OOP  object oriented Programming

# my_list = [ ]
# my_string = "Hello"

# my_list.append(1)
# my_string.append(1)  # cannot work as sting is not appendaple

# print(type(my_list))
# append(1) # cannot work as there is nothing to append to

# functions can stand alone, Methods need somthing to operate on.

# everything that is created is created by classes.  Everything is an object. 

# python is a object orientated class based programming lanuage

# so python is very good at oop (see above)


# Classes are always started with a Capital letter.len
# a class is a factory that creates objects. 
# class Car:
#      pass
 
#  print(Car())  The car has a position in memory so it is created. 
 
#  class List:
#      There are a set of behaviours and methods that can access and interact with the List
     
     
#  If we create our own class we can set our own rules on how it is interacted with.InterruptedError
#  OOP is very good at repication of real life attributes. e.g. colour, size, shape, strength etc.
 
     
# class Car:
def __init__(self, brand, color, model, year)   # a constructor or initializer.   So the class auto associates the methods.
    self.brand = brand
    self.model = model
    self.color = color
    self.year = year

car_1 = Car('Ford', 'grey', 'escort', '1990')
car_2 = Car('Alfa', 'red', 'Gino', '1963')

print(car_1.brand)
print(car_1.color)   # classes ar etemplates for building a standard object that complies with specific data.
# can create funtions that can apply to the class.

    car_1 = car()
    car_1.brand = 'Ford'
    car_1.model = 'escort'
    car_1.color = 'grey'
    car_1.year = 1990
        

  
  # methods are really functions of a class
def age(self):
    print(self.current_year - int(self.year))
    
def __str__(self):
    return f'The {self.brand} {self.model} is {self.color} built in {self.year}'   
  
def ignition(self):
    print('The car is on...') 
    
def drive(self):
    print('driving...')
    
def stop(self):
    print('stopping...')
    
def turning_off(self):
    print('turning off...' )
    
car_1.ignition()   
car_1.stop() 
car_1.drive()
car_1.turning_off()
print(str(car_1)) 



         
 
 
