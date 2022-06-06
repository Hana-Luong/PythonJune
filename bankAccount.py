class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        self.int_rate = 0.04
    def deposit(self, amount):
	    self.balance += amount
        return self
    def withdraw(self, amount):
	    self.balance -= amount
        if balance < 0 : 
            print(f"Insufficient funds: Charging a $5 fee")
            self.balance = balance - 5
        return self
	def yield_interest(self):
        if balance > 0 :
		    self.balance = balance * (1 + int_rate)
        return self
    def display_account_info(self):
		print(f"{self.account_number} has a balance of: {self.balance}")
        return self
# Create 2 accounts
lana = User("123456789", 10)
thang = User("987654321",100)

# make 3 deposits1, withdrawal, calculate with interest
# somewhere to put account number and interest rate
lana.deposit(100).deposit(200).deposit(50).withdraw(220).yield_interest().display_account_info())
#thang.deposit(100).deposit(20).deposit(50).withdraw(220).yield_interest().display_account_info())

