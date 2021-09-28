import os
import shutil

path = "text"
try:
    os.remove(path)
    #os.rmdir(path) to remove empty folders
    #first import shutil, shutil.rmtree(path) delete a dir containing files
except FileNotFoundError:
    print("File was not found!")
except PermissionError: #empty folders exception
    print("You don't have the permission to delete that!")
except OSError: # to handle deleting a dir with files
    print("You can not delete that using that function!")
else:
    print(path + " was deleted.")

