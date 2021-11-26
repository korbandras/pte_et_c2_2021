class BankAccount:
    def __init__(self, name: str, account_number: str, balance=0):
        self.name=name
        self.account_number=account_number
        self.balance=balance
    def print_balance(self):
        print(self.balance)
    def withdrawal(self,amount: int):
        if amount<=self.balance:
            self.balance-=amount
            print("Successful withdrawal")
        else:
            print("Unsuccessful withdrawal, not enough coverage!")
    def deposit(self,amount: int):
        self.balance+=amount
    def transfer(self,other,amount: int):
        if self.balance>=amount:
            self.balance-=amount
            other.balance+=amount
            print("Transfer completed")
        else:
            print("You can not transfer the given amount of money, you do not have enough coverage")