from car import Car

car_1 = Car("Chevy", "Corvette", 2021, "blue")

# we can also add another value to the class variable
car_1.wheels = 2  # now the value of the car wheels will be 2

print(car_1.wheels)
print(Car.wheels)
