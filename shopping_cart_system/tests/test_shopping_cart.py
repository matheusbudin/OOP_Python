import unittest
from shopping.item import Item
from shopping.shopping_cart import ShoppingCart

class TestShoppingCart(unittest.TestCase):
    def test_add_and_total_cost(self):
        cart = ShoppingCart()
        item1 = Item("Apple", 0.99)
        item2 = Item("Banana", 0.59)
        cart.add_item(item1)
        cart.add_item(item2)
        self.assertAlmostEqual(cart.total_cost(), 1.58)

if __name__ == '__main__':
    unittest.main()
