import random

alphabets = ["A","B" ,"C" , "D","E","F","G","H","I","J","K"]
symbols = ["@","#" ,"%" , "$","*","&","!"]
num = ["1","2","3","4","5","6","7","8","9"]


user_alpha = int(input("How many alphabets would you like"))
user_symbol = int(input("How many symbols"))
user_num = int(input("How many numbers do you need"))
password=""



for alpha in range(user_alpha):
    randAlpha = random.choice(alphabets)
    password+=randAlpha


for symbol in range(user_symbol):
    randSymbol = random.choice(symbols)
    password+=randSymbol

for numb in range(user_num):
    randNum = random.choice(num)
    password+=randNum


print("Your password" + " "+password )