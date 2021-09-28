#write inside the file

text = "This is added from here\n Hey!!!"

with open("text", "w") as file: #inside we add the name of the file, and add the function w-write, a-append
    file.write(text)
