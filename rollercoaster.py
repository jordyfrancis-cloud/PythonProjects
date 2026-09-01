print("Welcome to the rollercoaster")
height=int(input("Enter your Height ?:"))

if height >= 120:
    print("You can ride")
    age=int(input("What is your age ?"))

    if age <= 12:
        bill=5
        print("That will be $5")
    elif age <= 18:
        bill=7
        print("That will be $7")
    else:
        bill=12
        print("That will be $12")

    photos=input("Do you want to have a photo taken ? Type y for yes and n for No.")
    if photos=="y":
       bill += 3

    print(f"Your final bill is {bill}")
else:
    print("Sorry, You cannot ride.")


