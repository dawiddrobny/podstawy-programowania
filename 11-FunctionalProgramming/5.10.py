import matplotlib.pyplot as plt

temps = {"Krakow": 7, "Warszawa": -2, "Sopot": 4, "Koszalin": -1, "Opole": 3}

cities = list(temps.keys())
temperatures = list(temps.values())

plt.bar(cities, temperatures)
plt.title("Temperatures in Cities")
plt.xlabel("Cities")
plt.ylabel("Temperature (C)")
plt.show()
