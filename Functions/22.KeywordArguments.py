#keyword arguments = arguments prceded by an identifier when we pass them to a function
#                   the order of the arguments doesn't matter, unlike positional arguments
#                   python knows the names of the arguments that our function receives

def hello(first,middle,last):
    print("Hello" + first + middle + last) #the position is already set

hello(last="Halimi",first=" Armir",middle=" ") #using keyword arguments
