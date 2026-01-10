bottles = [508, 500, 512, 499, 492, 511, 503, 476, 501, 509]
capacity = 500
tolerance = 0.02

def is_incorrect(volume):
    return abs(volume - capacity) > capacity * tolerance

incorrect = list(filter(is_incorrect, bottles))
percentage = (len(incorrect) / len(bottles)) * 100

print(f"Bottle capacity:    {capacity}ml")
print(f"Filling tolerance:  {int(tolerance*100)}%")
print(f"Filled bottles:     {','.join(map(str, bottles))}")
print(f"Incorrectly filled: {int(percentage)}%")
