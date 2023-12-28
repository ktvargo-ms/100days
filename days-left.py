print("hello")
age = input("What is your current age?\n")
#age = 5
age_as_int = int(age)
years_remain = 90 - age_as_int     
days_remain = years_remain * 365
weeks_remain = years_remain * 52
months_remain = years_remain * 12
message = (f"You have {days_remain} days {weeks_remain} weeks and {months_remain} months remaining")
print(message)