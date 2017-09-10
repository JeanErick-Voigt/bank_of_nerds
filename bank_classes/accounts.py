#! /usr/bin/env/ python3
from decimal import Decimal

class Account():
	def __init__(self, account_name):
		self.account_record = {}
		self.account = account_name
		

	def create_account(self):
		self.account_record[self.account] = round(Decimal(0.0), 2)

	def deposit(self, money):
		money = round(Decimal(money), 2)
		if self.account in self.account_record:
			self.account_record[self.account] += money
		else:
			print("Account does not exist")
		return(0)

	def withdrawal(self, account_name, money):
		money = Decimal(money)
		if account_name in self.account_record:
			if self.account_record[self.account] < money:
				print("Do not have enough in account to withdraw")
			else:
				self.account_record[self.account] -= money

	def account_balance(self, account_name):
		result = ""
		if account_name in self.account_record:
			#result += (self.account_record[self.account]
			return(self.account_record[self.account])
		
		else:
			return("account does not exist")
		#return(result)
	#	else:
	#		print("Do not have this account")
	#		return(0)

if __name__ == "__main__":
	checking = Account("checking")
	checking.create_account()
	checking.deposit(Decimal(1.00))
	print(checking.account_balance("checking"))
	checking.withdrawal("checking", 10.00)
	print(checking.account_balance("checking"))
