arr = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]

print("Before swapping:")
for row in arr:
    for num in row:
        print(num, end=" ")
    print()

for row in arr:
    row[0], row[-1] = row[-1], row[0]

print("After swapping:")
for row in arr:
    for num in row:
        print(num, end=" ")
    print()
