import unittest
from shopping.item import Item

class TestItem(unittest.TestCase):
    def test_item_creation(self):
        item = Item("Apple", 0.99)
        self.assertEqual(item.get_price(), 0.99)

if __name__ == '__main__':
    unittest.main()
