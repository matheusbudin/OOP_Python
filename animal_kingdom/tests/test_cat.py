import unittest
from animals.cat import Cat

class TestCat(unittest.TestCase):
    def test_cat_sound(self):
        cat = Cat()
        self.assertEqual(cat.make_sound(), "Meow")

if __name__ == '__main__':
    unittest.main()
