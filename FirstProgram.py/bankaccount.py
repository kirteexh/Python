class Account:
    def __init__(self,bal,acc):
        self.balance = bal
        self.account_no = acc

    def deb(self,deb):
        self.balance -= deb
        print("Amount Debited =",deb)
        print("Balance =",self.balance)

    def cred(self,cred):
        self.balance += cred     
        print("Amount Credited =",cred)
        print("Balance =",self.balance)   

a1 = Account(1000,9746)
a1.deb(500)
a1.cred(100)      