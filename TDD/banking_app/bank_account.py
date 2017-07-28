class BankAccount:

    def __init__(self, balance=0):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, value=0):
        if not value:
            value = 0

        if value >= 0:
            self._balance += value
        else:
            raise ValueError('Deposit value must be a positive integer')

    def withdraw(self, value=0):
        if not value:
            value = 0

        # penalty for exceeding balance
        if value > self.balance:
            value += 5

        if value >= 0:
            self._balance -= value
        else:
            raise ValueError('Withdraw value must be a positive integer')
