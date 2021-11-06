#Task 4: Login functionality
# In its parameter list, define three parameters: database, username, and password.


def login(database, username, password):
    if username in dict.keys(database) and password in dict.values(database):
        print("Welcome back: ", username)
    elif username in dict.keys(database) or password in dict.values(database):
        print("Check your credentials again!")
    else:
        print("Something went wrong")

def register(database, username):
    if username in dict.values(database):
        print("Username already registered")
    else:
        print("Username successfully registered: ", username)

def donate(username):
    donation_amount = float(input("Enter an amount to donate: "))
    donation = print(username, " Has donated: ", donation_amount)
    print("Thank you for the donation!")

def show_donations(donations):
    print("\n--- All Donations ---")
    if donations == 0:
        print("Currently there are no donations yet!")
    else:
        print("List of donations: ", donations)

    print(sum(donations))
    
