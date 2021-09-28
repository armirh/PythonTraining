import random

#roll a dice
x = random.randint(1,6)
y = random.random() #floating numbers random

#generate a list
my_list = ['rock', 'paper', 'scissors']
z = random.choice(my_list)

#shuffle a deck of cards
cards = [1,2,3,4,5,6,7,8,9,10,'j','q','k','a']
random.shuffle(cards)

print(x)
print(y)
print(z)
print(cards)