#**kwargs = parameter that will pack all arguments into a dictionary
#        useful so that a function can accept a varying amount of keyword arguments
#naming is not important, just use **before hand

def hello(**kwargs):
    #print("Hello " + kwargs['first'] + " " + kwargs['last']), common way
    print("Hello", end=" ")
    for key,value in kwargs.items():
        print(value, end=" ")

hello(middle="Mr",first="Armir", last="Halimi") #so we can add as many keyword arguments as we want.

