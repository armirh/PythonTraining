# Classes inherit attributes and methods from another class, parent and children
# Benefit so we can just change the parent class

class Animal:

    alive = True

    def eat(self):
        print("This animal is eating!")
    def sleep(self):
        print("This animal is sleeping!")

# separate classes, to use inheritance inside the parenthesis we add the name of the other class
# And now Rabbit becomes the child class and Animal is the parent class, and will inherit everything from the Animal class
# these classes can also have their own unique methods apart from the one that they inherit

class Rabbit(Animal):
    def run(self):
        print("This rabbit is running!")
class Fish(Animal):
    def swim(self):
        print("This fish is swimming!")
class Hawk(Animal):
    def fly(self):
        print("This hawk is flying")

# create object from these classes
rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive)  # it gets the class variable alive, even though it hasn't been declared inside the rabbit class
fish.eat()
hawk.sleep()

rabbit.run()
fish.swim()
hawk.fly()



