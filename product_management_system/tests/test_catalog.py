import unittest
from product_management.product import Product
from product_management.catalog import Catalog
from product_management.pricing_strategy import StandardPricingStrategy

class TestCatalog(unittest.TestCase):
    def test_catalog_total_price(self):
        catalog = Catalog()
        catalog.add_product(Product("Product 1", 50))
        catalog.add_product(Product("Product 2", 150))
        strategy = StandardPricingStrategy()
        self.assertEqual(catalog.calculate_total_price(strategy), 200)

if __name__ == '__main__':
    unittest.main()
