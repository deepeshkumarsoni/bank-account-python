import unittest
from accounts.account import *

class AccountTest(unittest.TestCase):
    def I_Can_Get_Balance(self):
        """
        I can get balance from my account
        """
        account = Account()
        balance = account.getBalance()
        self.assertEqual(balance, 0)


if __name__ == '__main__':
    unittest.main()