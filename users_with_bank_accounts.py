class Bank_account:
    def __init__(self,balance = 0,int_rate=0.01):
        self.int_rate = int_rate
        self.balance = balance


    def deposit(self,amount):
        current_balance = self.balance
        new_balance = current_balance + amount
        self.balance = new_balance


    def withdraw(self,amount):
        curent_balance = self.balance
        new_balance=curent_balance - amount
        self.balance = new_balance


    def display_account_info(self):
        print("Your balance is",self.balance)
        print("your interest rate is ", self.int_rate)


    def yield_int_rate(self):
        if self.balance > 0:
            self.balance += self.int_rate* self.balance




class Users:
    def __init__(self,f_name,l_name,age):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.savings = Bank_account(balance=0,int_rate=0.01)


    def display_user_info(self):
        print("First name",self.f_name)
        print("Last name",self.l_name)
        print("Age",self.age)
        self.savings.display_account_info()


    def user_deposit(self,amount):
        self.savings.deposit(amount)


    def user_withdraw(self,amount):
        self.savings.withdraw(amount)


    def user_yield_int_rate(self):
        self.savings.yield_int_rate()


user = Users("Lenddy","Morales",18)
user.display_user_info()
user.user_deposit(500)
user.display_user_info()
user.user_withdraw(10)
user.display_user_info()
user.user_yield_int_rate()
user.display_user_info()