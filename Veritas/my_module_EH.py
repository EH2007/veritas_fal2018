import random
x = 10

"""def my_function():
    print("Hello")"""

rock = 1
paper = 2
scissor = 3

def computer_rps():
    dice = random.randrange(1,4)
    if you == "rock":
        if dice == rock:
            print("rock.")
        elif dice == scissor:
            print("scissor.")
        else:
            print("paper.")
    if you == paper:
        if dice == paper:
            print("paper.")
        elif dice == rock:
            print("rock.")
        else:
            print("scissor.")
    if you == scissor:
        if dice == scissor:
            print("scissor.")
        elif dice == paper:
            print("paper.")
        else:
            print("rock.")

computer_rps()
