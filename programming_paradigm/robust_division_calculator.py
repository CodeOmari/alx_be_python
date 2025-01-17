def safe_divide(numerator, denominator):
    try:
        float(numerator)
        float(denominator)
    except ValueError:
        return f"Error: Please enter numeric values only."

    try:
        float(denominator) > 0
        result = float(numerator)/float(denominator)
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return f"Error: Cannot divide by zero."
    