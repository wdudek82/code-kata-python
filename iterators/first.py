import string

# samp_str = iter("Sample")
#
# print("Char: {}".format(next(samp_str)))
# print("Char: {}".format(next(samp_str)))


class Alphabet:

    def __init__(self):
        self.letters = string.ascii_uppercase
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.letters) - 1:
            raise StopIteration
        self.index += 1

        return self.letters[self.index]


alpha = Alphabet()

for letter in alpha:
    print(letter)
