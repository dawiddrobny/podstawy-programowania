arr_2d = [
    [7, 3, 7, 9, 0],
    [2, 9, 0, 1, 5],
    [3, 8, 6, 4, 7],
    [8, 7, 1, 1, 5]
]

sum_last_col = 0
for row in arr_2d:
    sum_last_col += row[-1]

print("Sum of last column:", sum_last_col)
