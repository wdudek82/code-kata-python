import operator


# Forceing usage of keyword-only arguments - no positional arguments
# in place of keyword args are allowed
def safe_division_c(number, divisor, *,
                    ignore_overflow=False,
                    ignore_zero_division=False):
    try:
        # return operator.__truediv__(number, divisor)
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise


result = safe_division_c(5, 2, ignore_overflow=True, ignore_zero_division=True)
# result = safe_division_c(5, 2, True, True)
print(result)

