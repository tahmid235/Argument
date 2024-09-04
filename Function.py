def factorial(n):
    """
    Calculate the factorial of a non-negative integer n.
    
    Parameters:
    n (int): A non-negative integer whose factorial is to be calculated.
    
    Returns:
    int: Factorial of the number n.
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage
number = 5
result = factorial(number)
print(f"The factorial of {number} is {result}")
