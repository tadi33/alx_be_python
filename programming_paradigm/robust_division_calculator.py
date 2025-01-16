def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        denom = float(denominator)
        result = num / denom
        return result
    except ZeroDivisionError:
        return "Error: Denominator cannot be zero."
    except ValueError:
        return "Error: Both numerator and denominator must be numeric values."
    
