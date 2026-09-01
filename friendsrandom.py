import random

friends = ["Alice" , "Bob" , "Charlie" , "David" , "Emmanuel"]
random_choice = random.randint(0,4)

if random_choice == 0:
    print("Alice")
elif random_choice == 1:
    print("Bob")
elif random_choice == 2:
    print("Charlie")
elif random_choice == 3:
    print("David")
else:
    print("Emmanuel")




