# object is an instance of a class, combination of attributes and methods(actions)
# class is a blueprint, that will describe attributes and methods it has
# a naming convention for classes is that we use uppercase names for classes
# we can create our classes in separate modules, and then import it to other modules

from car import Car

# to create an object
car_1 = Car("Chevy", "Corvette", 2021, "blue") # and we pass in the arguments that we put in the object
# we can use the object more than once
car_2 = Car("VW", "Passat", 2020, "gray")

# to print out each element of the object
print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)

# use the methods
car_1.drive()
car_2.stop()



