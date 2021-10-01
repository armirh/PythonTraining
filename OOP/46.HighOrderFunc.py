# High Order Functions = a function that either:
#                       1. accepts a function as an argument
#                               or
#                       2. returns a function
#                       (In python, functions are also treated as objects)

# 1. accept a function as an argument
# we have two functions, that accept string arguments
def loud(text):
    return text.upper()


def quiet(text):
    return text.lower()


# the high order function
def hello(func):
    text = func("Hi")
    print(text)


# name of the higher order function, and a function as an argument
hello(loud)  # => uppercase
hello(quiet)  # => lowercase


# 2. Return a function

def divisor(x):
    def dividend(y):
        return y / x

    return dividend


divide = divisor(2)
print(divide(10))  # this is the dividend and goes y/x = > 5.0 output




