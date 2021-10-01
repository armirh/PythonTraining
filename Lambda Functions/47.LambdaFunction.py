# lambda function = function written in 1 line using lambda keyword
#                   accepts any number of argument, but only has one expression.
#                   (think of it as a shortcut)
#                   (useful if needed for a short period of time, throw-away)

# syntax
# lambda parameters:expression

# classic way of doing it
def double(x):
    return x * 2


print(double(5))

# using the lambda expression
double = lambda x: x * 2
multiply = lambda x, y: x * y
add = lambda x, y, z: x + y + z
full_name = lambda first_name, last_name: first_name + " " + last_name
age_check = lambda age: True if age >= 18 else False

print(age_check(17))
print(double(5))
print(multiply(6, 5))
print(add(3, 4, 5))
print(full_name("Armir", "Halimi"))
