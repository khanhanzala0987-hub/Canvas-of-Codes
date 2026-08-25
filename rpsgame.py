import random

threevalues = ["Rock", "Paper", "Scissors"]

robot = random.choice(threevalues)
print(robot)
player = input("Please Enter Rock or Paper or Scissors - ")

print(f"robot chose - {robot}")
print(f"player chose - {player}")

if player == robot:
    print("Tie Match")

elif player == "Rock" and robot == "Scissors":
    print("Congrats You Won")

elif player == "Paper" and robot == "Rock":
    print("Congrats You Won")

elif player == "Scissors" and robot == "Paper":
    print("Congrats You Won")

else:
    print("You lose")
