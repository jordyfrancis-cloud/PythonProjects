

print("Welcome to Treasure Island")
print("Your mission is to find the treasure")

direction=input("Left or Right").lower()

if direction=="right":
    print("You fell into a hole. Game over")
elif direction == "left":
    print("You have come to a lake: ")
    option=input("Swim or wait").lower()

    if option=="swim":
        print("Game over, you were attacked by a man eating crocodile")
    elif option=="wait":
        door=input("Which door? Red,Blue or yellow").lower()
        if door=="red":
            print("Game over")
        elif door=="blue":
            print("Game over")
        elif door=="yellow":
            print("Congrats you find the gold you win")
        else:
            print("This door doesn't exist: GAME OVER")

    else:
        print("Sorry we don't have that option")




else:
    print("Sorry not an option")