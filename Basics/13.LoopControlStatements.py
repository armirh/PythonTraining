#Loop control = change a loops execution from its normal sequence

# break - used to terminate the loop entirely
# continue - skips to the next iteration of the loop
# pass - does nothing, acts as a place holder

#if name not entered we break out of loop, and terminate completly
while True:
    name = input("Enter your name: ")
    if name != "":
        break

# in case the "-" is encountered in the loop, it skips it using the continue statement
phone_number = "123-456-7890"
for i in phone_number:
    if i == "-":
        continue
    print(i, end=" ")

print("\n") #acts a space between lines

#pass, just acts a place holder
for i in range(1,21):
    if i == 13:
        pass
    else:
        print(i, end=" ")

