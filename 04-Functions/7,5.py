from range_check import is_in_range

num = int(input("Enter a number: "))
x = int(input("Enter the lower bound: "))
y = int(input("Enter the upper bound: "))
result = "yes" if is_in_range(num, x, y) else "no"
print(f"Number {num} in the range <{x},{y}>: {result}")
