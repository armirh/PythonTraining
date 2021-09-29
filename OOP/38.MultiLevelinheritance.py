# Multi-level inheritance = a concept when a derived(child) class inherits
                                            # Another derived(child) class

# a hierarchy of classes

class Organism:

    alive = True

class Animal(Organism):
    def eat(self):
        print("This animal is eating!")

class Dog(Animal):
    def bark(self):
        print("This dog is barking!")

dog = Dog()
print(dog.alive)  # gets this from the Organism class
dog.eat()  # get this from Animal class
dog.bark()
