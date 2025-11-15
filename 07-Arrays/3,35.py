def transpose_matrix(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]

def print_matrix(matrix):
    for row in matrix:
        for num in row:
            print(num, end=" ")
        print()

matrices = [
    [[1, 2, 3], [4, 5, 6]],
    [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]],
    [[5, 6, 7, 8], [6, 7, 8, 9], [7, 8, 9, 0]]
]

for i, matrix in enumerate(matrices, 1):
    print(f"Matrix {i}:")
    print_matrix(matrix)
    print("Transposed:")
    print_matrix(transpose_matrix(matrix))
    print()