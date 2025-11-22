import re

with open("files.txt", "r", encoding="utf-8") as file:
    filenames = file.read().splitlines()

pattern = r".+\.\w{4}$"

for filename in filenames:
    if re.match(pattern, filename):
        print(filename)
