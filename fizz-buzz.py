print("This program is the Fizz Buzz game using numbers 1 to 100")

total = 0 
for number in range(0,101):
    if (number % 3 == 0) and (number % 5 == 0):
        print("FizzBuzz")
    elif (number % 3 == 0):
        print("Fizz")
    elif (number % 5 == 0):
        print("Buzz") 
    else:
        print(number)       
