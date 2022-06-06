# Create a file with the User class, including the __init__ 
class User:	
    def __init__(self, name):
        self.name = name
        self.account_balance = 0
# make_deposit method
    def make_deposit(self, amount):	
        self.account_balance += amount	
        return self
# Add a make_withdrawal method to the User class
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
# Add a display_user balance method to the User class
    def display_user_balance(self):
        print(f"{self.name} has a balance of {self.account_balance}")
        return self
# Create 3 instances of the User class
lana = User("Lana")
thang = User("Thang")
dieu = User("Dieu")
# Have the first user make 3 deposits and 1 withdrawal and then display their balance
lana.make_deposit(100).make_deposit(200).make_deposit(50).make_withdrawal(220).display_user_balance()
# BONUS: transfer_money(self, other_user, amount) - have this method decrease the user's balance by the amount and add that amount to other other_user's balance

