# zip(*iterables) = aggregates elements from two or more iterables(list,tuples,sets, etc.)
#                   creates a zip object with paired elements stored in tuples for each element

usernames = ['Armir', 'Jacob', 'Sam']
passwords = ('p@ssword', 'abc123', 'guest')
login_date = ['1/1/2021', '1/2/2021', '1/3/2021']

# we can also make this zip file into a dictionary or list using casting
# users = zip(usernames, passwords)
users = dict(zip(usernames, passwords))
print(type(users))

for key, value in users.items():
    print(key + " - " + value)

all_users = zip(usernames, passwords, login_date)

for i in all_users:
    print(i)


