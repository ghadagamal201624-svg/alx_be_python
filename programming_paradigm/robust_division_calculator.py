def safe_divide(numerator, denominator):
    try:
        num_flot = float(numerator)
        den_flot = float(denominator)
    except ValueError:
        return "false, Error: Please enter numeric values only."
    try:
        result = num_flot / den_flot
        return (true, result)
    except ZeroDivisionError:
        return (false, "Error: Cannot divide by zero.")
    except Exception as e:
        return (false, f"An unexpected error occurred-{str(e)}")
    
    