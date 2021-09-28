# nested function calls = function calls inside other function calls

#common way of doing it
#num = input("Enter a whole number: ")
#num = float(num)
#num = abs(num)
#num = round(num)
#print(num)

print(round(abs(float(input("Enter a whole number: "))))) #just in one line of code
