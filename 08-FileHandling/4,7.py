import re

text = input("Enter text: ")

vowel_pattern = r"[aeiouAEIOU]"
vowels = re.findall(vowel_pattern, text)
num_vowels = len(vowels)

print(f"Number of vowels: {num_vowels}")
