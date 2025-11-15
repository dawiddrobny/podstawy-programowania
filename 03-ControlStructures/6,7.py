age = int(input('Enter age: '))
age_group = ''
if age < 13:
    age_group = 'child'
elif age < 20:
    age_group = 'teenager'
elif age < 65:
    age_group = 'adult'
else:
    age_group = 'senior'
print(f'You are a {age_group}')
