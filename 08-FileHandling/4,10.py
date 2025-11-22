import csv

with open("clothing.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        price = float(row["Price"])
        stock = int(row["Stock_Quantity"])

        if price < 60 and stock < 40:
            print(
                f"{row['Product_Name']},{row['Category']},{row['Size']},{row['Color']},{row['Price']},{row['Stock_Quantity']}"
            )
