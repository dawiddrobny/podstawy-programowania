import json

try:
    with open('cities.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    print("Cities in Poland:")
    for city in data:
        for key, value in city.items():
            print(f"{key} : {value}")
        print("-" * 20)

except FileNotFoundError:
    print("cities.json not found.")
