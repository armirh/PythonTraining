import os

#hold the location where our file is located
source = 'text' #file path if needed
destination = "/Users/armirhalimi/Desktop/untitled folder" #destination where we want to move it,also rename it

try:
    if os.path.exists(destination):
        print("There is already a file there!")
    else:
        os.replace(source,destination)
        print(source+" was moved")
except FileNotFoundError:
    print("Source was not found !")

