row1 =["a","b","c"]
row2 =["d","e","f"]
row3 =["g","h","i"]
map =[row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
print(f"The first number is the column, and the second number is the row")
area = input("Where do you want to put the treasure? ")

# split the string to get the row and column numbers
row = int(area[0])
column= int(area[1])

#where in the map are we targeting
spot = map[column-1][row-1]
print(spot)

#identify the selected column
selected_column = map[column-1]

#identify the selected row on the selected column as 'X' marks the spot
selected_column[row-1] = "X"

#print the updated map
print(f"{row1}\n{row2}\n{row3}")