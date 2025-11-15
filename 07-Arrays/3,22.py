import random


def rand_elem(array):
    if not array:
        return None
    return array[random.randint(0, len(array) - 1)]


arr = [10, 20, 30, 40, 50]
print("Random elements:")
for _ in range(5):
    print(rand_elem(arr), end=" ")
print()
