import random
repeat = True
while repeat:
    print("You rolled", random.randint(1,6))
    print("Do you want to roll again? Y/N")
    repeat = ("y" or "yes") in input().lower()
else:
    print('Thank you for playing')