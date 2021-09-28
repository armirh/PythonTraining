#logical operators = used to check if two or more conditional statements is true

temp = int(input("What is the temperature outside?: "))

if temp >= 0 and temp <= 30: #with using and, both statements need to be true
    print("The temperature is good today!")
    print("Go outside!!")
elif temp < 0 or temp > 30: #if one of the statements if true, the statement gets executed
    print("The temperature is bad today!")
    print("Stay inside!")

#using not statement,kinda does the oposite of what we write next!
if not(temp >= 30 and temp <= 30):
    print("The temperature is bad today!")
    print("Stay inside!")
elif not(temp < 0 and temp > 30):
    print("The temperature is good today!")
    print("Go outside!!")
