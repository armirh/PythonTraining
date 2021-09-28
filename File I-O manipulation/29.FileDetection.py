#in order to do these functions we need this module
import os

path = "/"

if os.path.exists(path):
    print("That location exists")
    #check if that location is a file or not
    if os.path.isfile(path):
        print("That location is a file!")
    #check if that location is a file directory or a folder
    elif os.path.isdir(path):
        print("That location is a folder!")
else:
    print("That location does not exist")
