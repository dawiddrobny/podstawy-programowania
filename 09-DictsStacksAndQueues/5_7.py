hotels_in_Krakow = [
   {"name": "Sky", "price": 320.00},
   {"name": "Metropol", "price": 480.00},
   {"name": "New Port", "price": 420.00},
   {"name": "Aparthotel", "price": 390.00}
]

hotels_in_Sopot = [
   {"name": "Focus", "price": 510.00},
   {"name": "Aqua", "price": 345.00},
   {"name": "La Boutique", "price": 390.00},
   {"name": "Marina", "price": 410.00}
]

def hotel_list(hotels):
    return ", ".join([h["name"] for h in hotels])

def avg_price(hotels):
    if not hotels:
        return 0
    total = sum(h["price"] for h in hotels)
    return round(total / len(hotels))

krakow_avg = avg_price(hotels_in_Krakow)
sopot_avg = avg_price(hotels_in_Sopot)

print(f"Hotels in Krakow: {hotel_list(hotels_in_Krakow)}")
print(f"Average hotel price in Krakow: {krakow_avg}")
print(f"Hotels in Sopot: {hotel_list(hotels_in_Sopot)}")
print(f"Average hotel price in Sopot: {sopot_avg}")

if krakow_avg < sopot_avg:
    print("Cheaper hotels in: Krakow")
elif sopot_avg < krakow_avg:
    print("Cheaper hotels in: Sopot")
else:
    print("Prices are equal on average.")
