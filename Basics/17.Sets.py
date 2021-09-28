#sets = collection which is unordered, unindexed. No duplicate values

utensils = {"fork", "spoon", "knife", "knife"} #even if we put x2 knives, it still shows just one, no duplicates
dishes = {"bowl", "plate", "cup", "knife"}

#useful functions in sets
utensils.add("napkin")
#utensils.remove("knife")
#utensils.clear() - completly deletes the set
utensils.update(dishes) #puts the other set inside the first set
dinner_table = utensils.union(dishes) #basically unionize from both sets

print(utensils.difference(dishes)) #check the differences between utensils and dishes/ what utensils have that dishes don't
print(utensils.intersection(dishes)) #common elements between the two sets

#every time the set gets executed, the order changes
for x in dinner_table:
    print(x, end=" ")

