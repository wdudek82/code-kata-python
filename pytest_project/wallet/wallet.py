class Wallet:
    def __init__(self, initial_amount=0):
        self.balance = initial_amount

    def balance(self):
        return self.balance

    def add_cash(self, amount):
        self.balance += amount

    def spend_cash(self, amount):
        if self.balance < amount:
            msg = f'{amount} exceeds current amount of money in wallet!'
            raise InsufficientAmount(msg)
        self.balance -= amount


class InsufficientAmount(Exception):
    pass
