def f(x, y):
    count = 0
    for num in range(x, y):
        if num < 0 and num % 2 == 0:
            count += 1
    return count


print(f(-7, 8))
print(f(-1, 11))
