arr = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [
    0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

for i in range(5):
    for j in range(5):
        arr[i][j] = (i + 1) * (j + 1)

for row in arr:
    for num in row:
        print(f"{num:2}", end=" ")
    print()
