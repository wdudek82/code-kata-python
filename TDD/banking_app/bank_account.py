class BankAccount:

    def __init__(self):
        self._balance = 0

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

        if value >= 0:
            self._balance -= value
        else:
            raise ValueError('Withdraw value must be a positive integer')


if __name__ == '__main__':
    b = BankAccount()
    b.deposit = 50

    print(b.deposit)
