import time

# epoch problem, find when your computer thinks time began (Reference point)
print(time.ctime(1000000000))  # convert a time expressed in seconds since epoch to a readable string
print(time.time())  # seconds since epoch time

# current date and time
print(time.ctime(time.time()))

# another way
time_object = time.localtime()
print(time_object)
# we have to format the time object in order to show proper time/date
local_time = time.strftime("%B %d %Y %H: %H:%M:%S", time_object)
print(local_time)


time_string = "10 April 1997"
time_format = time.strptime(time_string, "%d %B %Y")
print(time_format)



# asc time function, tuple representation of a time, makes it readable
time_tuple = (2020, 4, 20, 4, 20, 0, 3, 5, 1)
time_string1 = time.asctime(time_tuple)
print(time_string1)


# mk time, convert it to seconds
time_tuple1 = (2020, 4, 20, 4, 20, 0, 3, 5, 1)
time_string2 = time.mktime(time_tuple)
print(time_string2)
