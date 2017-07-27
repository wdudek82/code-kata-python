class BankAccount:

    def __init__(self):
        self._deposit = 0

    @property
    def deposit(self):
        return self._deposit

    @deposit.setter
    def deposit(self, value):
        self._deposit = value


if __name__ == '__main__':
    b = BankAccount()
    b.deposit = 50

    print(b.deposit)
