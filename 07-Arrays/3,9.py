def compare(array1, array2):
    if len(array1) != len(array2):
        return False
    for i in range(len(array1)):
        if array1[i] != array2[i]:
            return False
    return True


test_cases = [
    (["water", "book", "sky"], ["water", "book", "sky"]),
    ([True, False], [True, False, True]),
    ([5, 3, 1], [5, 3, 1]),
    ([3, 2, 1], [3, 2])
]

for arr1, arr2 in test_cases:
    print("Array1:", end=" ")
    for item in arr1:
        print(item, end=" ")
    print()
    print("Array2:", end=" ")
    for item in arr2:
        print(item, end=" ")
    print()
    print("Comparison: arrays are the same" if compare(
        arr1, arr2) else "Comparison: arrays are not the same")
    print()
