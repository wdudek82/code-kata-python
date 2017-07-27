import unittest
from .bank_account import BankAccount


class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.acc = BankAccount()
        self.acc.deposit(50)
        balance = self.acc.balance
        self.assertEqual(balance, 50)

    def test_balance_direct_assignment(self):
        with self.assertRaises(AttributeError):
            self.acc.balance = 10

    def test_deposit_money(self):
        self.acc.deposit(50)
        balance = self.acc.balance
        self.assertEqual(balance, 100, f'Balance should equal 50, not {balance}')

    def test_deposit_negative_value_rises_value_error_exception(self):
        self.assertRaises(ValueError, self.acc.deposit, -10)

    def test_deposit_non_numeric_value_raises_type_error_exception(self):
        self.assertRaises(TypeError, self.acc.deposit, 'a')

    def test_deposit_empty_value(self):
        pass

    def test_deposit_none(self):
        pass

    def test_withdraw_money(self):
        self.acc.withdraw(30)
        balance = self.acc.balance
        self.assertEqual(balance, 20, 'Balance should equal 30')

    def tearDown(self):
        del self.acc


if __name__ == '__main__':
    unittest.main()
