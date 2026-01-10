class EBook:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 1
        self.is_open = False

    def open(self):
        self.is_open = True
    
    def close(self):
        self.is_open = False
    
    def next_page(self):
        if self.is_open:
            if self.current_page < self.pages:
                self.current_page += 1
        else:
            print("The book is closed")
    
    def previous_page(self):
        if self.is_open:
            if self.current_page > 1:
                self.current_page -= 1
        else:
            print("The book is closed")

    def show_status(self):
        print(f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}, Current page: {self.current_page}")
