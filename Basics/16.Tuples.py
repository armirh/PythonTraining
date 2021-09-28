#tuple - collection which are ordered and unchangable
#           used to group related data

student = ("Armir", "Halimi", 24, "male") #tuple created

#function related to tuples
print(student.count("Armir")) #check how many times is that value is mentioned
print(student.index(24)) #check the index where that value is located

for x in student:
    print(x, end=" ")

print("\n")

if "Armir" in student:
    print("He is here!")


#nested tuples
my_tuple = ("Armir", [8,4,6], (1,2,3))
print(my_tuple)