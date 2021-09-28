#string slicing, create a substring by extracting elements from another string
#2 ways of slicing: indexing[] or slice()
#                    [start:stop:step]

#indexing way of slicing
name = "Armir Halimi"
first_name = name[:5] #indexing the variable to create another one => Armir-output
last_name = name[6:] #[inclusive/exclusive]
funky_name = name[::2] #step, skip every second character
reversed_name = name[::-1] #reversing the variable(name)
print(reversed_name)
print(funky_name)
print(first_name)
print(last_name)


#slice function, create the object which is reuasble

website = "http://google.com"
website2 = "http://wikipedia.com"
slice = slice(7,-4) #we use negative indexing since a lot of website vary on the link size
print(website2[slice])
print(website[slice])




