import random 

print("Let's play Rock, Paper, Scissors\n")
your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors\n"))

rps_list = ["Rock", "Paper", "Scissors"]
print(f"Your choice is {rps_list[your_choice]}")

computer = random.randint(0,2)
print(computer)

print(f"The computer choice is {rps_list[computer]}\n")

if your_choice == 0 and computer == 2 :
    print("You win")
elif  your_choice > computer:
    print("You lose")
else:
    print("wrong answer.  you lose")
