# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Safely perform division with error handling for:
    - ZeroDivisionError
    - ValueError for non-numeric inputs
    """
    try:
        num = float(numerator)
        denom = float(denominator)

        if denom == 0:
            return "Error: Cannot divide by zero."

        result = num / denom
        return f"The result of the division is {result}"

    except ValueError:
        return "Error: Please enter numeric values only."
