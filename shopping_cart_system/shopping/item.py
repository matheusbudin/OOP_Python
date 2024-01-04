class Item:
    def __init__(self, name, price):
        self.__name = name   # private attribute
        self.__price = price # private attribute

    def get_price(self):
        return self.__price

    def __str__(self):
        return f"{self.__name}: ${self.__price}"
