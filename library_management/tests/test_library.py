import unittest
from library.book import Book
from library.library import Library

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.lib = Library()
        self.book1 = Book("1984", "George Orwell")
        self.lib.add_book(self.book1)

    def test_add_and_list_books(self):
        self.assertEqual(self.lib.list_books(), [self.book1])

    def test_is_book_available(self):
        self.assertTrue(self.lib.is_book_available("1984"))
        self.assertFalse(self.lib.is_book_available("Animal Farm"))

if __name__ == '__main__':
    unittest.main()
