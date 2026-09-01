print("Welcome to Pizza Deliveries!")
size=input("What size pizza do you want? S, M or L: ")
pepperoni= input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill=0

if size=="S":
    bill=15
    print("That will be $15")
elif size=="M":
    bill=20
    print("That will be $20")
elif size=="L":
    bill=25
    print("That will be $25")

else:
    print("Sorry not available")
    exit()

age=int(input("Enter your age"))
if age > 45 and age< 55:
    print("FreeTicket")
else:
    print("Sorry")





if pepperoni=="Y":
    if size == "S":
       bill +=2
       print("That will be extra 2 dollars")
    else:
        bill+=3

        print("That will be extra 3 dollars")

if extra_cheese=="Y":
    bill+=1



print("The total bill will be",bill)

