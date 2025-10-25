price = float(input("Enter price: "))
discount = float(input("Enter discount %: "))
discount_amount = price * discount / 100
print(f"Price with discount: {price - discount_amount:.2f}")
print(f"Reduction: {discount_amount:.2f}")
