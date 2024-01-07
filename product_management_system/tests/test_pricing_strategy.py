import unittest
from product_management.pricing_strategy import StandardPricingStrategy, DiscountPricingStrategy

class TestPricingStrategy(unittest.TestCase):
    def test_standard_pricing(self):
        strategy = StandardPricingStrategy()
        self.assertEqual(strategy.calculate_price(100), 100)

    def test_discount_pricing(self):
        strategy = DiscountPricingStrategy(10)  # 10% discount
        self.assertEqual(strategy.calculate_price(100), 90)

if __name__ == '__main__':
    unittest.main()
