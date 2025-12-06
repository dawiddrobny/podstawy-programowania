price_list = {
    'T-shirt': 19.99,
    'Jeans': 49.99,
    'Jacket': 89.99,
    'Sneakers': 59.99,
    'Hat': 15.99
}

print("Prices before discount:")
for item, price in price_list.items():
    print(f"{item}: {price:.2f}")

total_before = sum(price_list.values())
print(f"Total value before discount: {total_before:.2f}")

# Apply discount
for item in price_list:
    price_list[item] = round(price_list[item] * 0.90, 2)

print("\nPrices after 10% discount:")
for item, price in price_list.items():
    print(f"{item}: {price:.2f}")

total_after = sum(price_list.values())
print(f"Total value after discount: {total_after:.2f}")
