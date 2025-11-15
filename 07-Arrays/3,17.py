my_tuple = (50, 20, 40, 50, 30, 50)
value = 50
count = 0
for item in my_tuple:
    if item == value:
        count += 1
print("Tuple:", my_tuple)
print("Value:", value)
print("Number of occurrences:", count)
