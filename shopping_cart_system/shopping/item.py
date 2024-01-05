class Item:
    def __init__(self, name, price):
        self.__name = name   # private attribute
        self.__price = price # private attribute

    def get_price(self):
        return self.__price

    def __str__(self):
        return f"{self.__name}: ${self.__price}"
    @classmethod
    def with_default_price(cls, name):
        return cls(name, 1.0)  # default price is 1.0