# Abstract class = prevents a user from creating an object of that class, a ghost class.
# Compels a user to override abstract methods in a child class.

# abstract class = a class which contains one or more abstract methods.
# abstract method = a method that has a declaration but does not have an implementation.
# basically use from the parent and also override the go() method with their own implementation

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    # overriding abstract method
    def go(self):
        print("You drive the car")
    def stop(self):
        print("The car has stopped")

class Motorcycle(Vehicle):

    def go(self):
        print("You ride the motorcycle")
    def stop(self):
        print("The motorcycle has stopped")

#vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()

#vehicle.go()
car.go()
motorcycle.go()
#vehicle.stop()
car.stop()
motorcycle.stop()

