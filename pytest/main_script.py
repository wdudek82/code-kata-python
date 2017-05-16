

def capital_case(string):
    if not isinstance(string, str):
        raise TypeError("Please provide a string argument")
    return string.capitalize()


# if __name__ == "__main__":
#     print(capital_case("test string"))