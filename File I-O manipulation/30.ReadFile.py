#reading a file from outside, either use the path or if it is in within our project folder
# just use the name

#to prevent misstyping the file name we do the exception method
try:
    with open("text") as file:
        print(file.read())
except FileNotFoundError:
    print("The file was not found!")
