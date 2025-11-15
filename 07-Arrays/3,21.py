arr1 = [1, 3, 5]
arr2 = [1, 2, 3, 4, 5, 6, 7]
is_subset = True
for num in arr1:
    if num not in arr2:
        is_subset = False
        break
print("First array is subset of second:", is_subset)
