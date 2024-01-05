class ShoppingCart:
    def __init__(self, discount=None):
        self.items = []
        self.discount = discount  # Aggregation of Discount class

    def add_item(self, item):
        if ShoppingCart._validate_item_name(item):
            self.items.append(item)

    def total_cost(self):
        total = sum(item.get_price() for item in self.items)
        return self.discount.apply_discount(total) if self.discount else total

    @staticmethod
    def _validate_item_name(item):
        return isinstance(item, Item) and len(item.get_price()) > 0
