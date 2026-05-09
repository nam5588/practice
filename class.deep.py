"""CLASS deep diving
    (1) ENCAPSULATION
    (2) INHERITENCE
    (3) POLIMORPHISM
"""
print("======= ENCAPSULATION =======")
'''
C++, JAVA, PHP, TypeScript > public private protected
Python > public     __private       _protected
'''


class Account():
    # state
    description = "The class makes bank accounts"

    # constructor
    def __init__(self, owner, amount):
        self.__owner = owner
        self.__amount = amount

    # method
    def get_balance(self):
        print(f"the owner is {self.__owner} has {self.__amount} usd")

    def deposit(self, amount):
        print("deposit:", amount)
        self.__amount += amount

    def withdraw(self, amount):
        print("withdraw:", amount)
        self.__amount -= amount


my_account = Account("Shawn", 1000)
my_account.get_balance()
print('------')
my_account.deposit(5300)
my_account.withdraw(800)
my_account.get_balance()
print('------')


try:
    result = my_account.__amount
    print('result:', result)
except Exception as err:
    print('No target state found')
