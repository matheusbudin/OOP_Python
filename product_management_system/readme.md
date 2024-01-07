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

#Design pattern applied:

### Strategy Pattern in the Project

1. **Location**: 
   - Implemented in `pricing_strategy.py`.

2. **Description**:
   - The `PricingStrategy` abstract class defines a common interface for different pricing strategies.
   - There are two concrete implementations of this interface: `StandardPricingStrategy` and `DiscountPricingStrategy`.
   - These subclasses (`StandardPricingStrategy` and `DiscountPricingStrategy`) override the `calculate_price` method to provide specific pricing behaviors.

3. **Usage in the Project**:
   - The `Catalog` class uses a `PricingStrategy` to calculate the total price of products.
   - By passing different implementations of `PricingStrategy` to the `Catalog`, you can change the way prices are calculated without altering the `Catalog` class. This is a key feature of the Strategy Pattern – it allows algorithms to be selected at runtime.

4. **Benefits**:
   - This pattern provides flexibility in choosing the appropriate pricing algorithm.
   - It adheres to the open/closed principle, as new pricing strategies can be added without modifying existing code.
   - It encapsulates the pricing algorithm details from the `Catalog`, leading to a cleaner and more maintainable code structure.

### Example Usage in `main.py`:

In `main.py`, the Strategy Pattern is demonstrated when different pricing strategies are applied to the `Catalog`:

```python
standard_pricing = StandardPricingStrategy()
print("Total price with standard pricing:", catalog.calculate_total_price(standard_pricing))

discount_pricing = DiscountPricingStrategy(10)  # 10% discount
print("Total price with 10% discount:", catalog.calculate_total_price(discount_pricing))
