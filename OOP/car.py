# object can have attributes and methods

class Car:

    # class variable, is declared inside the class but outside the constructor
    wheels = 4  # in default all cars will have this value

    # special method that will construct objects for us, we don't need to pass a argument for self
    def __init__(self, make, model, year, color):
        self.make = make  # assign attributes
        self.model = model  # instance variable
        self.year = year
        self.color = color

    # different methods that class might contain
    def drive(self): # self refers to the object that is using this method
        print("This " + self.model + " is driving")

    def stop(self):
        print("This " + self.model + " has stopped")

