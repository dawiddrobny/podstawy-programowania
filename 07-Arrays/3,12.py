arr = [2, 3, 2, 5, 8, 1, 9, 8]
print("Array:", end=" ")
for num in arr:
    print(num, end=" ")
print()
print("Unique elements:", end=" ")
for i in range(len(arr)):
    is_unique = True
    for j in range(len(arr)):
        if i != j and arr[i] == arr[j]:
            is_unique = False
            break
    if is_unique:
        print(arr[i], end=" ")
print()
