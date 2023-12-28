print("This is the love calculator")
name1 = input("What is your name?\n")
name2 = input("What is their name?\n")
combined_name = name1 + name2
string_lower_combined = combined_name.lower()

t = string_lower_combined.count("t")
r = string_lower_combined.count("r")
u = string_lower_combined.count("u")
e = string_lower_combined.count("e")

true_count = t + r + u + e


l = string_lower_combined.count("l")
o = string_lower_combined.count("o")
v = string_lower_combined.count("v")
e = string_lower_combined.count("e")

love_count = l + o + v + e

total_score = int(str(true_count) + str(love_count))

print(f"Your love count is {total_score}")

if (total_score < 10) or (total_score > 90):
    print("wow")
