def calculate_discount(price: float, discount_rate: float) -> float:
    """Calculate the discounted price given the original price and discount rate."""
    # Avoid using a negative discount rate
    if discount_rate < 0:
        raise ValueError('Discount rate cannot be negative')
    return price * (1 - discount_rate)

# Example usage:
discounted_price = calculate_discount(100, 0.2)
print(f'Discounted price: {discounted_price}')