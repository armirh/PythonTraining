#nested loops = The "inner loop" will finish all of it's iteration
#               before finished the "outter loop"
# basically a loop inside another loop

rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol = input("Choose the symbol you want to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()



