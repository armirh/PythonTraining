#if statements = a block of code that will execute only if it's condition is true

age = int(input("How old are you?: "))

# you add as much needed conditions in the program, it gets executed line by line!!
if age >= 18:
    print("You are an adult!")
elif age < 0:
    print("You haven't been born yet!")
elif age == 100:
    print("You are a century old!")
else:
    print("You are a minor!")