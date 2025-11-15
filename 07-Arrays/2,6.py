
matrix = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

for i in range(len(matrix)):
    matrix[i][i] = 1

# Print the modified array
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()
