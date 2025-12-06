person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming", "excursions"],
    "married": True,
    "phone": {"landline": "123444321", "mobile": "777888999"}
}

print(f"Name: {person['name']}")

print(f"Hobby: {person['hobby']}")

print(f"Entire dictionary: {person}")

person['surname'] = 'Nowak'

person['married'] = not person['married']

person['gender'] = 'male'

person['hobby'].append('bicycle')

person['phone']['work'] = '313131444'

print("\nUpdated dictionary content:")
for key, value in person.items():
    print(f"{key} : {value}")
