from abc import ABC, abstractmethod

class PricingStrategy(ABC):
    @abstractmethod
    def calculate_price(self, base_price):
        pass

class StandardPricingStrategy(PricingStrategy):
    def calculate_price(self, base_price):
        return base_price

class DiscountPricingStrategy(PricingStrategy):
    def __init__(self, discount_rate):
        self.discount_rate = discount_rate

    def calculate_price(self, base_price):
        return base_price * (1 - self.discount_rate / 100)
