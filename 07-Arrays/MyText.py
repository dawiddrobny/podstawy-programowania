def word_count(text):
    words = text.split()
    return len(words)


def words_by_length_desc(text):
    words = text.split()
    words.sort(key=len, reverse=True)
    return ",".join(words)


def words_alphabetically(text):
    words = text.split()
    words.sort(key=str.lower)
    return ",".join(words)
