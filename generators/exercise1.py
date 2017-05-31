from itertools import islice


def first_letters(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1


test_string = "This is only for tests"
result = first_letters(test_string)

for index, item in enumerate(result):
    # if index >= 3:
    #     break
    print(index, item)