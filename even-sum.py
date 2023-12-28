print("This program prints the sum of all even numbers, 1 to 100")

total = 0 
for number in range(0,101):
    if number % 2 == 0:
        #print(number)
        total += number
print(f"The total of the even number from 1 to 100 is {total}")        