class Acciunt :
    def __init__(self,balance):
        self._balance  = balance
    def getBalance(self):
        return self._balance

class CheckingAccount:
    numberOfAccount= 0
    def __init__(self,balance=0.0):

        self._balance = balance
        CheckingAccount.numberOfAccount  +=1
        
  
        

    def __str__(self):
        return f"Account Balance: {self._balance}"    


print('Number of Checking Accounts: ', CheckingAccount.numberOfAccount)
print(CheckingAccount())
print(CheckingAccount(100.00))
print(CheckingAccount(200.00))
print('Number of Checking Accounts: ', CheckingAccount.numberOfAccount)
        
