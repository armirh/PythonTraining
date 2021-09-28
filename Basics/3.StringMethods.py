#useful string methods

name = "Armir"

print(len(name)) #determine the length of our name
print(name.find("A")) #find the index of that letter
print(name.capitalize()) #capitalize your name, only first letter
print(name.upper()) #every character is upercase
print(name.lower()) #every character is lowercase
print(name.isdigit()) #to determine if that variable contain numbers
print(name.isalpha()) #to check if our name have only letters, *no spaces
print(name.count("r")) #count how many time that letter is repeated
print(name.replace("r", "rr")) #replace a particular letter inside that variable
print(name*3) #print the name 3 times

