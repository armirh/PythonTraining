# *args = paramater that will pack all arguments into a tuple
#           useful so that a function can accept a varying amount of arguments

def add(*args): #we can name the args in anything, we just need the * infront of the name
    sum = 0
    args = list(args) #cast the tuple into a list, so we can use indexing
    args[0] = 0
    for i in args:
        sum +=i
    return sum

print(add(1,2,3,4,5,6,7)) #useful so we can use any amount of arguments