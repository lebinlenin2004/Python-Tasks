class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.__balance = balance
        
    def deposit(self,amount):
        self.__balance = self.__balance + amount
        
    def check_balance(self):
        print("Your Balance is :",self.__balance)
        


Customer1 = BankAccount("Lebin",0)
print(Customer1.name)
Customer1.deposit(2000)
Customer1.deposit(1000)
Customer1.check_balance()

        
