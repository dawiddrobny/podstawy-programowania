arr = [7, 9, 2, 4, 5, 6]
print("arr =", arr)
i = 0
for j in range(len(arr)):
    if arr[j] % 2 == 0:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
print("arr =", arr)
