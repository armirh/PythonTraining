# ----
# if __name__ == '__main__'
# ----

# 1. Module can be run as a standalone program
# 2. Module can be imported and used by other modules

# Python interpreter set 'special variables', one of which is __name__
# then python will execute the code found within __main__
# the initial module being run

import mod2

if __name__ == '__main__':
    print("Running this module directly!")
else:
    print("Running other modules")

print(__name__)
print(mod2.__name__)
