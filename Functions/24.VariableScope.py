#scope = that region that a variable is recognized
#       A variable is only available from inside that region it is created
#       A global and locally scoped version of a variable can be created
# in case the variable name isn't changed inside the local scope it is used the global one
# the python rule of LEGB / Local, Enclosing,Global,Built-in variables


name = "Armir H" #global scope, can be used inside and outside any function

def display_name():
    name = "Armir"  #local scope, only works inside this function
    print(name)

display_name()
print(name)

