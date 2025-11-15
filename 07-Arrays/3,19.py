arr = [15.5, 8.2, 31.7, 47.1, 2.3, 19.8]
value = float(input("Enter value: "))
count = 0
for num in arr:
    if num > value:
        count += 1
print(f"Number of elements greater than {value}: {count}")
