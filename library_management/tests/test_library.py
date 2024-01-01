from library.book import Book
from library.library import Library

def test_add_and_list_books():
    lib = Library()
    book1 = Book("1984", "George Orwell")
    lib.add_book(book1)
    assert lib.list_books() == [book1]

def test_is_book_available():
    lib = Library()
    book1 = Book("1984", "George Orwell")
    lib.add_book(book1)
    assert lib.is_book_available("1984") == True
    assert lib.is_book_available("Animal Farm") == False
