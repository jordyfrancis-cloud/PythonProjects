import random

print("Welcome to Rock , Paper , Scissors game")
game = ["rock" , "paper" , "scissors"]

your_choice = input("Choose : ").lower()

computer_choice = random.choice(game)
print(computer_choice)


if your_choice == computer_choice:
    print("No one wins")
elif your_choice == "rock" and computer_choice == "paper":
    print("You lose")
elif your_choice == "scissors" and computer_choice == "paper":
    print("You win")
elif your_choice == "rock" and computer_choice == "scissors":
    print("You win")
elif your_choice == "paper" and computer_choice == "rock":
    print("You win")
elif your_choice == "paper" and computer_choice == "scissors":
    print("you lose")
elif your_choice == "scissors" and computer_choice == "rock":
    print("you lose")
else:
    print("You typed an invalid word , you lose")



