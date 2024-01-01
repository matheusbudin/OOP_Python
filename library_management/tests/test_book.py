from library.book import Book

def test_book_initialization():
    book = Book("1984", "George Orwell")
    assert book.title == "1984"
    assert book.author == "George Orwell"
