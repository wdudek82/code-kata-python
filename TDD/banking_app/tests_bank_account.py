import unittest
from .bank_account import BankAccount


class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.acc = BankAccount()
        self.acc.deposit(50)
        self.assertEqual(self.acc.balance, 50)

    def test_balance_direct_assignment(self):
        with self.assertRaises(AttributeError):
            self.acc.balance = 10

    def test_deposit_money(self):
        self.acc.deposit(50)
        self.assertEqual(self.acc.balance, 100)

    def test_deposit_negative_value_rises_value_exception(self):
        self.assertRaises(ValueError, self.acc.deposit, -10)

    def test_deposit_non_numeric_value_raises_type_exception(self):
        self.assertRaises(TypeError, self.acc.deposit, '10')

    def test_deposit_empty_value(self):
        self.acc.deposit()
        self.assertEqual(self.acc.balance, self.acc.balance)

    def test_deposit_none(self):
        self.acc.deposit(None)
        self.assertEqual(self.acc.balance, self.acc.balance)

    def test_withdraw_money(self):
        self.acc.withdraw(30)
        self.assertEqual(self.acc.balance, 20, 'Balance should equal 30')

    def test_withdraw_null_doesnt_change_balance(self):
        self.acc.withdraw(None)
        self.assertEqual(self.acc.balance, self.acc.balance)

    def test_withdraw_nothing_doesnt_change_balance(self):
        self.acc.withdraw()
        self.assertEqual(self.acc.balance, self.acc.balance)

    def test_withdraw_string_raises_type_exception(self):
        self.assertRaises(TypeError, self.acc.withdraw, '10')

    def test_withdraw_negative_value_raises_value_exception(self):
        self.assertRaises(ValueError, self.acc.withdraw, -10)

    def tearDown(self):
        del self.acc


if __name__ == '__main__':
    unittest.main()