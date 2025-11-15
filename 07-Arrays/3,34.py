def identity_matrix(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


def print_matrix(matrix):
    for row in matrix:
        for num in row:
            print(num, end=" ")
        print()


print("Identity matrix 3x3:")
print_matrix(identity_matrix(3))
print()
print("Identity matrix 5x5:")
print_matrix(identity_matrix(5))
print()
print("Identity matrix 8x8:")
print_matrix(identity_matrix(8))
