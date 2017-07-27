import unittest
from .bank_account import BankAccount


class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.bank_account = BankAccount()

    def test_bank_account_deposit_money(self):
        self.bank_account.deposit = 50

    def tearDown(self):
        self.bank_account = None



if __name__ == '__main__':
    unittest.main()
