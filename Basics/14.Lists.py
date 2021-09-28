#list - used to store multiple items in a single variable

food = ["pizza", "hamburger", "pasta","hot-dog"] #each element can be targeted using the index
#you can add or change elements within a list
food[0] = "sushi" #use indexing and change the list
print(food)
print(food[0])#access an element from the list using indexing
print(food[1])

print("\n")
#print elements of a list using for loop
for i in food:
    print(i,end=" ")

#useful list functions, first type the name of the list and . to access functions
food.append("ice cream") # add another element to the end of the list
food.remove("hot-dog") # remove certain element using its name
food.pop() # removes last element of the list
food.insert(0,"cake") #adds element using indexing
food.sort() #sorts alphabetically
food.clear() #removes the list completly
print(food)

