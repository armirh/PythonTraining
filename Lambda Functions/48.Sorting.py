# sort() method = used with lists
# sort() function = used with iterables

# this method is only viable with lists, built-in.
students = ["Armir", "Mike", "Sam", "Diana"]
students.sort()  # regular sorting, A-Z
students.sort(reverse=True)  # if we use keyword argument, Z-A in this case

# using sort function
sorted_students = sorted(students)
sorted_students1 = sorted(students, reverse=True)

for i in sorted_students:
    print(i)
print("\n")
for i in students:
    print(i)

# 2. A list of tuples, columns and rows
list_students = [("Sam", "F", 28),
                 ("Mike", "A", 33),
                 ("Armir", "B", 20),
                 ("Diana", "C", 24)]

# in order to sort this comes the key keyword argument, equal to a function that is going to return the index of that
# specific column

# sorting list by grade
grade = lambda grades: grades[1]
list_students.sort(key=grade)
# list_students.sort(key=grade,reverse=True)

# sorting list by age
age = lambda ages: ages[2]
list_students.sort(key=age)
# list_student.sort(key=age, reverse=True)

for i in list_students:
    print(i)


# 3. A tuple of tuples
list_students1 = (("Sam", "F", 28),
                  ("Mike", "A", 33),
                  ("Armir", "B", 20),
                  ("Diana", "C", 24))

age = lambda ages: ages[2]
sort_student = sorted(list_students1, key=age)



