class Discount:
    def __init__(self, percent):
        self.percent = percent

    def apply_discount(self, total):
        return total * (1 - self.percent / 100.0)
