def bubble_sort(arr):
    array = arr.copy()
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


def second_largest(array):
    sorted_array = bubble_sort(array)
    return sorted_array[-2]


def difference_max_min(array):
    sorted_array = bubble_sort(array)
    return sorted_array[-1] - sorted_array[0]


def median(array):
    sorted_array = bubble_sort(array)
    n = len(sorted_array)
    if n % 2 == 1:
        return sorted_array[n // 2]
    else:
        mid1 = sorted_array[n // 2 - 1]
        mid2 = sorted_array[n // 2]
        return (mid1 + mid2) / 2


def min_max_array(array):
    sorted_array = bubble_sort(array)
    return [sorted_array[0], sorted_array[-1]]


def array_to_string(array):
    result = ""
    for num in array:
        result += str(num) + "-"
    return result[:-1] if result else ""
