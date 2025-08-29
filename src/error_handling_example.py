def divide(x: float, y: float) -> float:
    """Divide x by y, returning None if y is zero."""
    if y == 0:
        print('Error: Cannot divide by zero!')
        return None
    return x / y

# Example usage:
result = divide(10, 0)
if result is not None:
    print(f'Result: {result}')