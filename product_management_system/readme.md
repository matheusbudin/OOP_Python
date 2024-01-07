Project fodler hierarchy:
product_management_system/
│
├── product_management/
│   ├── __init__.py
│   ├── product.py
│   ├── electronic_product.py
│   ├── food_product.py
│   ├── pricing_strategy.py
│   └── catalog.py
│
├── tests/
│   ├── __init__.py
│   ├── test_product.py
│   ├── test_electronic_product.py
│   ├── test_food_product.py
│   ├── test_pricing_strategy.py
│   └── test_catalog.py
│
└── main.py  # The script demonstrating the use of your classes

how to run the tests: 
`python -m unittest discover -s tests`

how to run the main.py that prints the examples in the terminal:
`python -m unittest discover -s tests`

All the concepts covered regarding OOP in this project:
### OOP Concepts in the Project

1. **Inheritance and Polymorphism**
   - *Location*: `product.py`, `electronic_product.py`, `food_product.py`
   - *Description*: `ElectronicProduct` and `FoodProduct` inherit from the base `Product` class and override the `display_info` method, demonstrating polymorphism.

2. **Encapsulation**
   - *Location*: Across all classes
   - *Description*: Internal state of objects (like name and price in `Product`) is kept private and exposed through public methods.

3. **Composition**
   - *Location*: `catalog.py`
   - *Description*: The `Catalog` class manages a collection of `Product` instances, illustrating composition.

4. **Strategy Pattern**
   - *Location*: `pricing_strategy.py`
   - *Description*: Abstract class `PricingStrategy` with subclasses `StandardPricingStrategy` and `DiscountPricingStrategy` demonstrate the Strategy design pattern.

5. **Class Methods and Static Methods**
   - *Description*: Can be included in classes for utility purposes. Example: static methods for validation or class methods for creating instances with default settings.

6. **Aggregation**
   - *Description*: Not explicitly shown but can be illustrated similarly to composition in `Catalog`, with a less tightly coupled relationship, like associating a `Discount` class instance with `Catalog`.

7. **Main Script (`main.py`)**
   - *Description*: Utilizes the classes and their methods to demonstrate practical application of OOP concepts.
