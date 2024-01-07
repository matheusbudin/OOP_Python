
import unittest
from product_management.food_product import FoodProduct 

class TestFoodProduct(unittest.TestCase):
    def test_display_info(self):
        product = FoodProduct("Apple", 1)
        self.assertEqual(product.display_info(), "Food Product - Apple, Base Price: 1")

if __name__ == '__main__':
    unittest.main()
