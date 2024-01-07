from product_management.product import Product
from product_management.electronic_product import ElectronicProduct
from product_management.food_product import FoodProduct
from product_management.pricing_strategy import StandardPricingStrategy, DiscountPricingStrategy
from product_management.catalog import Catalog

def main():
    # Create some products
    generic_product = Product("Generic", 20.0)
    laptop = ElectronicProduct("Laptop", 1000.0)
    apple = FoodProduct("Apple", 2.0)

    # Display product info
    print(generic_product.display_info())
    print(laptop.display_info())
    print(apple.display_info())

    # Create a catalog and add products
    catalog = Catalog()
    catalog.add_product(generic_product)
    catalog.add_product(laptop)
    catalog.add_product(apple)

    # Apply standard pricing
    standard_pricing = StandardPricingStrategy()
    print("Total price with standard pricing:", catalog.calculate_total_price(standard_pricing))

    # Apply discount pricing
    discount_pricing = DiscountPricingStrategy(10)  # 10% discount
    print("Total price with 10% discount:", catalog.calculate_total_price(discount_pricing))

if __name__ == "__main__":
    main()
