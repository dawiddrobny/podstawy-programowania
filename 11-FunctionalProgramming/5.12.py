medals = [
    {"country": "Denmark", "gold": 2, "silver": 4, "bronze": 6},
    {"country": "Finland", "gold": 5, "silver": 0, "bronze": 4},
    {"country": "USA", "gold": 12, "silver": 5, "bronze": 11},
    {"country": "Peru", "gold": 0, "silver": 1, "bronze": 7}
]

at_least_10 = list(filter(lambda c: c["gold"] + c["silver"] + c["bronze"] >= 10, medals))

print("COUNTRIES WITH AT LEAST 10 MEDALS")
for c in at_least_10:
    print(f"{c['country']}: {c['gold']},{c['silver']},{c['bronze']}")
