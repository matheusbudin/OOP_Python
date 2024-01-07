import unittest
from product_management.product import Product

class TestProduct(unittest.TestCase):
    def test_product_creation(self):
        product = Product("Generic Product", 10.0)
        self.assertEqual(product.display_info(), "Product: Generic Product, Base Price: 10.0")

if __name__ == '__main__':
    unittest.main()
