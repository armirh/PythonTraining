#exception = events detected during execution that interrupt the flow of the program
# every error that might occur during the problem we put it inside the try function
# check terminal to get specific errors, good practice to catch specific ones

try:
    numertaror = int(input("Enter a number to divide: "))
    denomintaor = int(input("Enter a number to divide by: "))
    result = numertaror/denomintaor
except ZeroDivisionError as e:
    print(e)
    print("You can not divide a number by 0!!")
except ValueError as e:
    print(e) #this tells the error type, optional
    print("You can only use numbers!!")
else:
    print(result)
finally:
    print("This will execute all the time, whether an error will occur!")
