filename = input("File name: ")

try:
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()

    lines = content.splitlines()
    num_lines = len(lines)

    num_characters = len(content)

    words = content.split()
    num_words = len(words)

    print(f"Number of lines: {num_lines}")
    print(f"Number of characters: {num_characters}")
    print(f"Number of words: {num_words}")

except:
    print(f"Error: File '{filename}' not found.")
