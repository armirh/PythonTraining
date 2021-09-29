# method chaining = is used to call multiple methods sequentially
#                   each call performs an action on the same object and returns self

class Car:

    def turn_on(self):
        print("You start the engine!")
        return self

    def drive(self):
        print("You drive the car!")
        return self

    def brake(self):
        print("You brake the car!")
        return self

    def turn_off(self):
        print("You stop the car!")
        return self


# classic way
car = Car()
car.turn_on().drive()  # to do method chaining, we have to add return self at the end of the method
car.brake().turn_off()

# all 4 methods
# car.turn_on().drive().brake().turn_off()

# better way, of chaining all 4 of the methods
car.turn_on() \
    .drive() \
    .brake() \
    .turn_off()
