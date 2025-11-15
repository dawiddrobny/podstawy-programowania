ean13 = input("Enter EAN-13 article number: ")

if len(ean13) == 13 and ean13.isdigit():
    print("Article number is correct")
    if ean13.startswith("590"):
        print("Article manufactured in Poland")
else:
    print("Invalid article number")
