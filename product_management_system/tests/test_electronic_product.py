import unittest
from product_management.electronic_product import ElectronicProduct

class TestElectronicProduct(unittest.TestCase):
    def test_display_info(self):
        product = ElectronicProduct("Laptop", 1000)
        self.assertEqual(product.display_info(), "Electronic Product - Laptop, Base Price: 1000")

if __name__ == '__main__':
    unittest.main()
