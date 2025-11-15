def bubblesort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array


test_arrays = [
    [7, 3, 8, 5, 2],
    [1, 4, 2, 8, 3],
    [9, 1, 7, 3, 6]
]

for arr in test_arrays:
    print("Original:", arr)
    sorted_arr = bubblesort(arr.copy())
    print("Sorted:", sorted_arr)
    print()
