from letters import count_letter


text = input("Enter text: ")
cnt = count_letter(text, "e")
print(f"The letter 'e' appears {cnt} times in the text.")
