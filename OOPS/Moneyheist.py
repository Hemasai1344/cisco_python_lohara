class Account:
    def __init__(self, number, name, minimum_bal = 1000):
        self.__number = number
        self.__name = name
        self.__balance = minimum_bal

    def __repr__(self):
        return f'[number = {self.__number}, name = {self.__name}, balance={self.__balance}]'
    
    def __str__(self):
        return self.__repr__()
    
    def deposit(self,amount):
        if amount<=0:
            print("Enter the Positive amount sir/mam")
            return
        self.__balance+=amount
    
    def withdraw(self,amount):
        #Abstraction
        if amount<=0:
            print("Enter the Positive amount sir/mam")
            return
        if amount >= self.__balance:
            print("No enough balance")
            return
        #Encapsulation
        self.__balance-=amount
    
aman_ac = Account(name='Aman Singh',number='9996667779991', minimum_bal=280000)
print(aman_ac)

aman_ac.deposit(1)
print(aman_ac)

aman_ac.withdraw(-86000)
print(aman_ac)

aman_ac.withdraw(200000)
print(aman_ac)

print(aman_ac.__dict__)