# map() = applies a function to each item in an iterable (list,tuple, etc.)
# ----- accepts two arguments
# map(function,iterable)

store = [("Sam", 20.00),
         ("Mike", 33.00),
         ("Armir", 50.00),
         ("Diana", 10.00)]

to_euros = lambda data: (data[0], round(data[1]*0.82))
to_dollars = lambda data: (data[0], round(data[1]/0.82))

store_euros = list(map(to_euros, store))
store_dollars = list(map(to_dollars, store))

for i in store_euros:
    print(i)

for i in store_dollars:
    print(i)




