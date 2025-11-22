with open("pets.txt", "r") as file:
    total = 0
    for line in file:
        total += len(line.split())
        print(line, end="")
    print(f"\nTotal number of words: {total}")
