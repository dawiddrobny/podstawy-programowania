amount = int(input("Enter the amount in PLN: "))

num_5 = amount // 5
remaining = amount % 5

num_2 = remaining // 2
remaining = remaining % 2

num_1 = remaining

print(f"\nThe amount of PLN {amount} in coins:")
print(f"5 PLN coins: {num_5}")
print(f"2 PLN coins: {num_2}")
print(f"1 PLN coins: {num_1}")
