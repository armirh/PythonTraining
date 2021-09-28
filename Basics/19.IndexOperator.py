# index operator [] = give access to a sequence's element (Str,list,tuples)

name = "armir Halimi!"
#access the first index and check if it is lowercase, and then switch it to uppercase
if(name[0].islower()):
    name = name.capitalize()
print(name)

#creating substring using indexing
first_name = name[:6].upper()
last_name = name[6:].capitalize()
last_char = name[-1] #just last character using negative indexing

print(last_char)
print(last_name)
print(first_name)
