class Account:
    def __init__(self):
        self.balance = 0
        
    def getBalance(self) :
        return self.balance

    def getdeposite(self,x):
        self.balance= x
        return self.balance

    def getwithdraw(self,y):
        self.balance -= y
        return self.balance

