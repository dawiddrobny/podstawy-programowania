from ebook import EBook

def main():
    book = EBook("The Hobbit", "J.R.R. Tolkien", 310)
    book.open()
    book.show_status()
    book.next_page()
    book.next_page()
    book.next_page()
    book.show_status()
    book.close()
    book.next_page()

if __name__ == "__main__":
    main()
