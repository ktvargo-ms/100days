print("Welcome to the roller coaster!")
height = int(input("What is your height in centimeters?"))
if height >= 120: 
    print("You can ride the roller coaster!")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Your ticket costs $5")
    elif age <= 18:
        bill = 8
        print("Your ticket costs $8")
    else:
        bill = 12
        print("Your ticket caosts $10") 
        
    wants_photo = input("Do you want a photo?  Y or N\n")    
    if wants_photo == "Y":
        bill = bill +3
        print(f"Your cost is ${bill}")    
    else: 
        print(f"Your cost is ${bill}")    
    
else:
    print("You are not tall enough to ride the roller coaster")    
