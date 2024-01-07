from .product import Product

class FoodProduct(Product):
    def display_info(self):
        return f"Food Product - {self.name}, Base Price: {self.base_price}"
