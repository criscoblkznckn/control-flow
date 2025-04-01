def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount if it is 20% or higher.
    :param price: Original price of the item.
    :param discount_percent: Discount percentage to apply.
    :return: Final price after applying the discount or the original price if discount < 20%.
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    return price

try:
    price = float(input("Enter the original price: "))
    discount_percent = float(input("Enter the discount percentage: "))
    
    final_price = calculate_discount(price, discount_percent)
    
    print(f"Final price: ${final_price:.2f}")
except ValueError:
    print("Invalid input. Please enter numeric values.")
