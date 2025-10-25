###
# A program that calculates
# how many letters are between two given letters
#
first = input("Enter first letter: ")
last = input("Enter last letter: ")
first_letter_code = ord(first)
number_of_letters = ord(last) - ord(first)
if number_of_letters > 0:
    number_of_letters -= 1
print(f"Between {first} and {last} is {number_of_letters} letters")
