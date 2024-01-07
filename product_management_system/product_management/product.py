class Product:
    def __init__(self, name, base_price):
        self.name = name
        self.base_price = base_price

    def display_info(self):
        return f"Product: {self.name}, Base Price: {self.base_price}"
