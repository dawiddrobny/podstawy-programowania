import csv


def get_genre_filename(genre):
    genre_mapping = {
        "Fantasy": "books_fantasy.txt",
        "Historical": "books_historical.txt",
        "Romance": "books_romance.txt",
        "Classic": "books_classic.txt",
    }
    return genre_mapping.get(genre)


def read_books():
    books = []
    with open("books.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            books.append(row)
    return books


def write_books_to_file(books, filename):
    with open(filename, "w", encoding="utf-8") as file:
        for book in books:
            line = f"{book['Title']},{book['Author']},{book['Genre']},{book['Year']}\n"
            file.write(line)


def organize_books_by_genre():
    books = read_books()

    genre_groups = {}
    for book in books:
        genre = book["Genre"]
        if genre not in genre_groups:
            genre_groups[genre] = []
        genre_groups[genre].append(book)

    for genre, genre_books in genre_groups.items():
        filename = get_genre_filename(genre)
        if filename:
            write_books_to_file(genre_books, filename)


organize_books_by_genre()
