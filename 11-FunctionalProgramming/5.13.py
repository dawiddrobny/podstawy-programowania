import matplotlib.pyplot as plt

medals = [
    {"country": "Denmark", "gold": 2, "silver": 4, "bronze": 6},
    {"country": "Finland", "gold": 5, "silver": 0, "bronze": 4},
    {"country": "USA", "gold": 12, "silver": 5, "bronze": 11},
    {"country": "Peru", "gold": 0, "silver": 1, "bronze": 7}
]

countries = list(map(lambda c: c["country"], medals))
total_medals = list(map(lambda c: c["gold"] + c["silver"] + c["bronze"], medals))

plt.bar(countries, total_medals)
plt.title("Total Medals by Country")
plt.xlabel("Country")
plt.ylabel("Number of Medals")
plt.show()
