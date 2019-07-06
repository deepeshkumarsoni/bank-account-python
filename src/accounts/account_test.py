import unittest
import account

class testaccount(unittest.TestCase):
    def Get_Balance(self):
        """
        I can get balance from my account
        """
        # Arrangement
        #account = getattr Account()

        # Action
        balance = Account.getBalance()

        # Assert
        self.assertEqual(balance, 0)


if __name__ == '__main__':
    unittest.main()