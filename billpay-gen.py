import random 

print("Welcome to the bill pay generator")
names_string = input("Enter the list of names using comma and spaces between names\n")
names_list = names_string.split(", ") 

lucky_winner = random.choice(names_list)
print(f"The lucky winner is {lucky_winner}.  You get to buy everyone's meal")

##alternate solution
#get the number of tiems in list and subtract 1 
#print that item in the list
num_items = len(names_list)
random_choice = random.randint(0, num_items -1)
#print(random_choice)
print(f"The lucky winner is {names_list[random_choice]}.  You get to buy everyone's meal")