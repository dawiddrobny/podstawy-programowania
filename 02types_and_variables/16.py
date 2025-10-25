###
# A program that prints a university abbreviation
#
university = "Krakow University of Economics"
for word in university.split():
    if word[0].isupper():
        print(word[0], end="")
