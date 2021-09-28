# str.format() = optional method that gives user more control in displaying output

animal = "cow"
item = "moon"

#traditional way of doing it
print("The " + animal +" jumped over the " + item)

#formatting way of doing it
print("The {} jumped over the {}".format(animal,item)) # the {} are called format fields
#                                                        they go in order, so animal first in our case
#                                                        and then item, but the output is the same.

print("The {0} jumped over the {1}".format(animal,item)) #positional arguments
print("The {animal} jumped over the {item}".format(animal="cow",item="moon")) #keyword arguments

text = "The {} jumped over the {}"
print(text.format(animal,item)) #another way of doing it

#ways of formatting text
print("The cow jumped over the {}".format(item))
print("The cow jumped over the {:10}".format(item))
print("The cow jumped over the {}".format(item))
print("The cow jumped over the {:^10}".format(item))

#formatting numbers

number = 1200

print("The number pi is {:.2f}".format(number)) #print only 2 decimals numbers
print("The number is {:,}".format(number)) #add , to the number
print("The number is {:b}".format(number)) #binary function
print("The number is {:o}".format(number)) #octal
print("The number is {:x}".format(number))

