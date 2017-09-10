#! /usr/bin/env python3
from decimal import Decimal
from bank_classes.accounts import Account

class Customer():
	def __init__(self):
		y = 1
		first_name = input("print your full name:  ")
		self._first_name = first_name
		while(y):
			if (self._first_name).isnumeric() or len(self._first_name) < 3:
				print("Name contained numbers, Invalid")
				self._first_name = input("print your name")
				print(self._first_name)
			else:
				y = 0
		
		self.accounts = []
		self.account_list = {}

	@property
	def name(self):
		return self._first_name

	@name.setter
	def name(self, first_name):
		if len(first_name) < 3 or first_name.isnumeric():
			name(first_name)
		self._first_name = first_name

	def create_account(self, account_type):
		account = Account(account_type)
		account.create_account()
		account.deposit(55.10)
		(self.accounts).append(account)
		return(account)		

	def deposit(self, money, account):
		for i in set(self.accounts):
			if account == i.account:
				i.deposit(money)
				break
		else:
			print("x{} is not a valid account".format(account))					
		return account
	
	def withdrawal(self, money, account):
		for i in set(self.accounts):
			if account == i.account:
				i.withdrawal(account, money)
				break
		else:
			print("{} is not a valid account to withdraw from".format(account))	

	def show_accounts(self):
		print("in show accounts function")
		print("{} accounts".format(self._first_name))
		if not self.accounts:
			print("No accounts to show")
		else:
			for i in self.accounts:
				if(i == "None"):
					print("No accounts")
				else:
					print(i)

	def loop(self):
		for i in self.accounts:
			print(i.account)
			print(i.account_record[i.account])
			print(i.account_balance(i.account))


	def __str__(self):
		result = ""
		if not self.accounts:
			result += ("Customer: {} has No accounts to show".format(self._first_name))

		else:	
			for i in self.accounts:
				#print(type(i))
				account_balance = round(Decimal(i.account_balance(i.account)), 2)
				result = result + str(i.account) + " " + str(account_balance)
				result += "\n"
		return(result)








if __name__ == "__main__":
	aron = Customer()
	test = "test"
	aron.deposit(30.00, test)
	checking = aron.create_account("Checking")
	IRA = "retirment"
	check = "Checking"	
	savings = aron.create_account("savings")
	save = "savings"
	aron.deposit(30.00, check)
	aron.deposit(5.00, IRA)
	aron.withdrawal(10.15, check)
	aron.deposit(2.00, save)
	print("This is after you add an account")
	print(aron)
