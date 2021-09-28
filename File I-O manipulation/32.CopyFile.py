# copyfile() = copies contents of a file
# copy() = copyfile + permission mode + destination can be directory
# copy2() = copy + copies metadata (file's creation and modification times)
# important to add shutil module

import shutil

shutil.copyfile("text", "copy.txt")#source,direction(if needed)