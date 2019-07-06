import unittest
from account import Account
account=Account()

class Test_account(unittest.TestCase):

    def test_Balance(self):      

        self.assertEqual(account.getBalance(), 0)

    def test_Deposite(self):
        self.assertEquals(account.getdeposite(100),100)
    
    def test_withdraw(self): 
        self.assertEquals(account.getdeposite(100),100)
        self.assertEquals(account.getwithdraw(10),90)
        

if __name__ == '__main__':
    unittest.main()