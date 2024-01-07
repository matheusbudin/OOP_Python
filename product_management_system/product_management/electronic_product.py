from .product import Product

class ElectronicProduct(Product):
    def display_info(self):
        return f"Electronic Product - {self.name}, Base Price: {self.base_price}"
