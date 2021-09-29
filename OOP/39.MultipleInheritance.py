# Multiple inheritance = when a chile class is derived from more than one parent class

class Prey:
    def flee(self):
        print("This animal flees!")

class Predator:
    def hunt(self):
        print("This animal hunting!")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Predator,Prey):
    pass

rabbit = Rabbit()  # this object has only access to the flee method, Prey
hawk = Hawk()   # this object has only access to the hunt method, Predator
fish = Fish()  # this object has access to both hunt/flee, Prey+Predator

rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()



