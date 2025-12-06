import json

try:
    with open('dogs.json', 'r', encoding='utf-8') as file:
        dogs = json.load(file)

    print("Dogs younger than 5 years:")
    for dog in dogs:
        if dog['age'] < 5:
            print(f"Name: {dog['name']}, Age: {dog['age']}, Breed: {dog['breed']}")

except FileNotFoundError:
    print("dogs.json not found.")
