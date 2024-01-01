from .book import Book

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        return self.books

    def is_book_available(self, title):
        return any(book.title == title for book in self.books)
