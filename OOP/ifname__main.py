# ----
# if __name__ == '__main__'
# ----

# 1. Module can be run as a standalone program
# 2. Module can be imported and used by other modules

# Python interpreter set 'special variables', one of which is __name__
# then python will execute the code found within __main__
# the initial module being run


def myfunction():
    print("This is a function")


if __name__ == '__main__':
    print("Executed directly")
else:
    print("Executed when imported")

myfunction()
