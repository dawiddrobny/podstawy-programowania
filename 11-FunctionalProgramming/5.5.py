numbers = list(range(1, 21))
divisible = list(filter(lambda x: x % 2 == 0 and x % 3 == 0, numbers))
print(divisible)
