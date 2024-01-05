import unittest
from shopping.discount import Discount

class TestDiscount(unittest.TestCase):
    def test_apply_discount(self):
        discount = Discount(10)  # 10% discount
        discounted_price = discount.apply_discount(100)  # Apply to $100
        self.assertEqual(discounted_price, 90)  # Expect $90 after discount

if __name__ == '__main__':
    unittest.main()
