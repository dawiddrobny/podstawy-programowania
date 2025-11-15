def convert_2d_to_1d(matrix):
    result = []
    for row in matrix:
        for num in row:
            result.append(num)
    return result


matrices = [
    [[2, 3], [1, 5]],
    [[5, 0, 3, 7, 5], [9, 0, 9, 1, 2]],
    [[2, 1], [3, 5], [7, 4], [2, 6]]
]

for i, matrix in enumerate(matrices, 1):
    print(f"Matrix {i}:")
    for row in matrix:
        for num in row:
            print(num, end=" ")
        print()
    print("1D array:", convert_2d_to_1d(matrix))
    print()
