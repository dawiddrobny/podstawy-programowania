def count_letter(text, letter, case_sensitive=False):
    if case_sensitive:
        return text.count(letter)
    return text.lower().count(letter.lower())
