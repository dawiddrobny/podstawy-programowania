hours_parked = int(input('Enter the number of hours parked: '))
cost = 0
if hours_parked >= 1 and hours_parked <= 2:
    cost = 5
elif hours_parked >= 3 and hours_parked <= 6:
    cost = 15
else:
    cost = 20
print(f'The cost of parking is {cost}')
