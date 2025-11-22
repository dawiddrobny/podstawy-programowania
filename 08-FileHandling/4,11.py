with open("powers.txt", "w", encoding="utf-8") as file:
    for num in range(1, 101):
        second_power = num**2
        third_power = num**3
        line = f"{num},{second_power},{third_power}"
        print(line)
        file.write(line + "\n")
