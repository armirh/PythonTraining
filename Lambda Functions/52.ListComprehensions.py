# list comprehension = a way to create a new list with less syntax
#                      can mimic certain lambda functions, easier to read
#                      list = [expression for i in iterable]
#                      list = [expression for i in iterable if conditional] if cases
#                      list = [expression (if/else) for item in iterable] if/else cases

squares = []                    # create an empty list
for i in range(1,11):           # create a for loop
    squares.append(i * i)       # define what each loop iteration should do
print(squares)

# with list comprehension
squares1 = [i * i for i in range(1, 11)]
print(squares1)


# example 2
students = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]

# using lambda
# passed_students = list(filter(lambda x: x >= 60, students))
# print(passed_students)

# with list comprehension, if statement
# passed_students = [i for i in students if i >= 60]
# print(passed_students)

# with list comprehension, else case added
passed_students = [i if i >= 60 else "Failed" for i in students]
print(passed_students)



