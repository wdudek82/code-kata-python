
def capital_case(string):
    if not isinstance(string, str):
        raise TypeError('Please provide a string argument')
    return string.capitalize()
