current_price = float(input("Enter current product price: "))
previous_price = float(input("Enter previous product price: "))

print(f"Current product price: {current_price:.2f}")
print(f"Previous product price: {previous_price:.2f}")

if previous_price > 0:
    percentage_drop = ((previous_price - current_price) / previous_price) * 100
    if percentage_drop >= 10:
        print("Buy the product!!")
        print(f"Product price reduced by {int(round(percentage_drop))}%")
