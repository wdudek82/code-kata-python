class FibIterator:

    def __init__(self):
        self.a = 1
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.a >= 10**2:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return self.b


fib = FibIterator()

for num in fib:
    print(num)

