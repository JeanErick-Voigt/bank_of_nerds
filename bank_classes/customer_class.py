#! /usr/bin/env python3
from decimal import Decimal
from bank_classes.accounts import Account

class Customer():
	def __init__(self):
		first_name = input("print your first name:  ")
		self._first_name = first_name
		self.accounts = []
		#self._last_name = last_name
		#self._DOB = DOB
		self.account_list = {}

	@property
	def name(self):
		return self._first_name


	def create_account(self, account_type):
		account = Account(account_type)
		account.create_account()
		account.deposit(55.10)
	#	print("type of current_account", type(account))
		(self.accounts).append(account)
		#self.account_list[current_account] = 1.00
		#(self.accounts).append(account_type)
		return(account)		

	def deposit(self, money, account):
		for i in set(self.accounts):
		#	print("This is account", account)
		#	print("This is i.account", i.account)
			if account == i.account:
				i.deposit(money)
				break
		else:
			print("x{} is not a valid account".format(account))					
		#(self.accounts).append(account)
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

#	def __str__(self):
#		result = ""
#		if not self.account_list:
#			result += ("Cusomter: {} has No accounts to show".format(self._first_name))
#		else:
#			result = ("Customer: {}".format(self._first_name))
#			result = result + "\n" + "accounts" + "\n"
#			for key, value in self.account_list:
#				result = result + key + value
#				result += "\n"
#
#		return(result)

	def loop(self):
		for i in self.accounts:
		#	print(type(i))
			print(i.account)
			print(i.account_record[i.account])
		#	print(type(self.accounts))
			#print(i[i.account])
			print(i.account_balance(i.account))


	def __str__(self):
		result = ""
		if not self.accounts:
			result += ("Customer: {} has No accounts to show".format(self._first_name))

		else:	
			#result = ("Customer: {}".format(self._first_name))
			#result = result + "\n" + "accounts" + "\n"
			for i in self.accounts:
				#print(type(i))
				account_balance = round(Decimal(i.account_balance(i.account)), 2)
				result = result + str(i.account) + " " + str(account_balance)
				result += "\n"
		return(result)






#	def account_list(self):
#		return(accounts)


	

	#@name.setter
	#def name(self, first_name):
	#	self._first_name = first_name

if __name__ == "__main__":
	aron = Customer()
#	print(aron.name)
#	aron.show_accounts()
#	print(aron)
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
#	aron.create_account("Saving")
	print("This is after you add an account")
#	aron.show_accounts()
	print(aron)
#	aron.loop()
