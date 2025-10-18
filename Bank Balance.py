class BankAccount:

           def __init__(self,owner,balance):
              self.owner = owner    
              self__balance = balance
              
           def bygetter(self):
             return self_balance

           def bysetter(self,amount):
              if amount>=0:
                  self._balance = amount
               else:
               print("Invalid amount")

obj = BankAccount("Imran".2200)

print(obj.bygetter())

obj.bysetter(54000)     
print(obj.bygetter())    
