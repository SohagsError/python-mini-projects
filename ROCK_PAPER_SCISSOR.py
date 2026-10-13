import random

def Robot():
    selected = random.choice(["ROCK", "PAPER", "SCISSOR"])
    return selected

robot = Robot()
userList = ['ROCK', 'PAPER', 'SCISSOR']

while True:
    user = input("Select ROCK or PAPER or SCISSOR: ").upper()

    if user in userList:
        break
    else:
        print("Please select between ROCK, PAPER OR SCISSOR only!Next time...")


if user == robot:
    print("You selected: ", user, " | Robot selected: ", robot)
    print("It's a tie! Try again...")
elif user == "ROCK" and robot == "SCISSOR":
    print("You selected: ", user, " | Robot selected: ", robot)
    print("You win! Yeeee...")
elif user == "PAPER" and robot == "ROCK":
    print("You selected: ", user, " | Robot selected: ", robot)
    print("You win! Yeeee...")
elif user == "SCISSOR" and robot == "PAPER":
    print("You selected: ", user, " | Robot selected: ", robot)
    print("You win! Yeeeee...")
else:
    print("You selected: ", user, " | Robot selected: ", robot)
    print("OPPSSS....You Lost!")    