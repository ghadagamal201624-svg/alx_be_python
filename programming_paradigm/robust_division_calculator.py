def safe_divide(numerator, denominator):
    try:
        num_flot = float(numerator)
        den_flot = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."
    try:
        result = num_flot / den_flot
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except Exception as e:
        return f"An unexpected error occurred: {e}"
    