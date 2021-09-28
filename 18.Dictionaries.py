# dictionary = A changeable, unordered collection of unique key:value pairs
#               fast because they use hashing, allow us to access a value quickly
#               key:value

capitals = {"USA":"Washington D.C",
            "Kosova":"Prishtina",
            "France":"Paris",
            "Germany":"Berlin"}
#since they are unordered we use they key to access the value
print(capitals["France"]) #if we use this method we would get an error if we use an itema that doesn't exist
print(capitals.get("Germany"))
capitals.update({"Russia":"Moscow"}) #add a new element to the dictionary
capitals.update({"Kosova":"Prizren"}) #also, we can change exisitng elements
capitals.pop("France") #removes a ceratin element
#capitals.clear()#clears everything

#useful functions in dictionary
print(capitals.values()) #print only the values
print(capitals.keys()) #print only the key

#prints entire dictionary
for key,value in capitals.items():
    print(key,value)




