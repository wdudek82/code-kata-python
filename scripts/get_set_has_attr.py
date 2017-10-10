class Experiment:

    total = 620.00
    tax_rate = 0.06
    reward_discount = 0.05

    def get_amount(self, *args, **kwargs):
        """ Get amount and return it somehow. """
        return {'amount': self.total}

    def get_tax(self, *args, **kwargs):
        return {
            'tax_rate': self.tax_rate,
            'tax_amount': self.total * self.tax_rate
        }

    def unknown(self, *args, **kwargs):
        return 'Unknown operator %s' % kwargs['operator']

    def get(self, operator=None):
        handler = getattr(self, 'get_%s' % operator, self.unknown)
        return handler(operator=operator)


if __name__ == '__main__':
    e = Experiment()

    op = 'tax'
    fun = e.get(operator=op)

    print(fun)

    hs = hasattr(Experiment, 'get_%s' % op)
    print(hs)

    setattr(Experiment, 'foo', 123)
    print(e.foo)

    # bar = lambda x, y: y ** 2

    def bar(x, y):
        y *= 2
        y = str(y) + 'aaa'
        return y

    setattr(Experiment, 'baz', bar)

    print(e.baz(2))
    print(e.baz(12))

