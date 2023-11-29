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
class Car:
    current_year = 2023  # Assume a current year for the age calculation

    def __init__(self, brand, color, model, year):
        # Constructor to initialize the object with provided values
        self.brand = brand
        self.model = model
        self.color = color
        self.year = year

    def age(self):
        # Method to calculate and print the age of the car
        print(self.current_year - int(self.year))

    def __str__(self):
        # Special method that defines the string representation of the object
        return f'The {self.brand} {self.model} is {self.color} and was built in {self.year}'

    def ignition(self):
        # Method to simulate turning the car on
        print('The car is on...')

    def drive(self):
        # Method to simulate driving the car
        print('Driving...')

    def stop(self):
        # Method to simulate stopping the car
        print('Stopping...')

    def turning_off(self):
        # Method to simulate turning the car off
        print('Turning off...')


# Creating instances of the Car class
car_1 = Car('Ford', 'grey', 'Escort', '1990')
car_2 = Car('Alfa', 'red', 'Gino', '1963')

# Accessing and printing attributes of car_1
print(car_1.brand)
print(car_1.color)

# Calling methods to simulate car actions
car_1.ignition()
car_1.stop()
car_1.drive()
car_1.turning_off()

# Printing the string representation of car_1 using the __str__ method
print(str(car_1))


# Encapsulation: Classes allow you to encapsulate data (attributes) and functionality (methods) together. This makes it easier to organize and manage your code.

# Abstraction: You can abstract away complex logic into methods. For example, the drive() method could involve a series of complex actions like checking fuel levels, engine status, etc.

# Reusability: Once you've defined a class, you can create multiple instances (objects) with different attributes. This is useful for modeling real-world entities where you might have many instances of the same kind of thing (e.g., multiple cars).

# Inheritance: You can create subclasses that inherit attributes and methods from a parent class. This promotes code reuse and helps in creating a hierarchy of related classes.

# Polymorphism: Different objects can respond to the same method call in different ways. This is particularly powerful when dealing with a collection of objects of different types that share a common interface.