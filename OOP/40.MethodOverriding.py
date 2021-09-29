class Animal:

    def eat(self):
        print("This animal is eating!")

class Rabbit(Animal):

    # method overriding is ability of an oop, to allow a subclass(child) provide a specific method
    # we should use the same name of the method, same parameters
    def eat(self):
        print("This rabbit is eating a carrot!")

rabbit = Rabbit()
rabbit.eat()