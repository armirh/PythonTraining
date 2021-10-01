# filter() = creates a collection of elements from an iterable for which a function returns true
# filter(function, iterable)

friends = [("Armir", 23),
           ("Jacob", 21),
           ("Reagan", 19),
           ("Sierra", 22)]
# syntax age = function, iterable = friends
# filter(age, friends)

age = lambda data: data[1] >= 18
drinking_buddies = list(filter(age, friends))

for i in drinking_buddies:
    print(i)





