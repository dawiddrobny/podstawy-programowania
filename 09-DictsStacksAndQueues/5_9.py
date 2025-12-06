import csv

provinces = {}

with open('province.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    for row in reader:
        if row:
            provinces[row[0]] = row[1]

province_counts = {name: 0 for name in provinces.values()}


with open('vehicle.txt', 'r') as f:
    for line in f:
        plate = line.strip()
        if plate:
            letter = plate[0]
            if letter in provinces:
                province_name = provinces[letter]
                province_counts[province_name] += 1

for province, count in province_counts.items():
    print(f"{province}: {count}")
