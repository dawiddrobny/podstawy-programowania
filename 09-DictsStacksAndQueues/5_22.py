import json

product = {}

product['name'] = input("Enter product name: ")
product['price'] = round(float(input("Enter product price: ")), 2)

paid_input = input("Paid (yes/no): ").lower()
product['paid'] = True if paid_input == 'yes' else False

file_name = "product.json"
with open(file_name, 'w', encoding='utf-8') as f:
    json.dump(product, f, indent=4)

print(f"Product saved to {file_name}")
