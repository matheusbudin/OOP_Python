class Catalog:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def calculate_total_price(self, pricing_strategy):
        return sum(pricing_strategy.calculate_price(p.base_price) for p in self.products)
