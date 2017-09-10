#! /usr/bin/env python3

from decimal import Decimal
from bank_classes.customer_class import Customer
#from customer_class import Customer



class Bank():
#	person = Customer()
	def __init__(self, bank_name):
		self._bank_name = bank_name
		self.customers = []

	@property
	def name(self):
		return self._bank_name

	def add_customer(self, Customer):
		return(self.customers.append(Customer))

	def customers_list(self):
		result = ""
		for i in self.customers:
			result = result + "\n" +  i.name
		print("Customer List")
		return(result)
		
	def get_customer_accounts(self, person):
		if person in self.customers:
			return(person)


				
			
		
	
	def deposit(self, person, account_type):
		print("How much would you like to Deposit")
		money = input()
		
		count = 0
		digit_count = 0
		output = "0"
		for i in money:
			digit_count += 1
			if i == ".":
				count += 1
				digit_count = 0
		if(count > 1):
			output = "2"
		elif(digit_count > 2):
			output = "1"
	

		value = output
		if value == "1":
			print("to many digits after decimals. Please re-enter")
			self.deposit(person, account_type)
		elif value == "2":
			print("Too many decimal points.  Please re_enter")
			self.deposit(person, account_type)
		else:	
			money = round(Decimal(money), 2)	
			person.deposit(money, account_type)
	
	
	def withdrawal(self, person, account_type):
		print("How much would you like to withdraw")
		money = input()
			
		count = 0
		digit_count = 0
		output = "0"
		for i in money:
			digit_count += 1
			if i == ".":
				count += 1
				digit_count = 0
		if(count > 1):
			output = "2"
		elif(digit_count > 2):
			output = "1"


		value = output
				
		if value == "1":
			print("to many digits after decimals. Please re-enter")				
			self.withdrawal(person, account_type)
		elif value == "2":
			print("Too many decimal points.  Please re_enter")
			self.withdrawal(person, account_type)
		else:	
			money = round(Decimal(money), 2)	
			person.withdrawal(money, account_type)

	
	#	person.withdrawal(money, account_type)	

	def __str__(self):
		result = ""
		print("*" * 30, "Inside str function")
		result = ("Full list of bank clieints and info\n")
		li = []
		if(not self.customers):
			return("No clients at this bank")
		for i in self.customers:
			li.append(i)
		for i in li:
			result +=  "Name: {0} \t Accounts: \n{1}".format(i.name, str(i))
			result += "\n"
		return result
	
	def test():
		print("Created")	


if __name__ == "__main__":
#	print("Test")
	bank1 = Bank("Bank of America")
#	test()
#	person = create_customer(self)
	#person1 = Customer()
	aron = Customer()
	#bank1.add_customer(person1)
	bank1.add_customer(aron)
	savings = aron.create_account("savings")
	checking = aron.create_account("checking")
	save = "savings"
	check = "checking"
	#aron.deposit(1.10, savings)
	bank1.deposit(aron, save)
	print("\n\n\n\n")
	print(bank1.customers_list())
	bank1.withdrawal(aron, check)
	print("\n\n\n\n")
	print("Accounts ", bank1.get_customer_accounts(aron))

#	print(aron)


#	print(bank1)
#	bank1.add_person_account(person2, "Savings")
#	bank1.add_person_account(person2, "Checking")



#	print(bank1)

#	print(str(person))
	#print(Bank1.name)
	#print("This is person being printed", person.name)
#	person.add_account("Saving")
#	print("Adding customer now")
#	Bank1.add_customer(person)
#	print("This is second customer")
#	Bank1.show_customers()
#	print("/n/nAdd 2nd  customer information")
#	print("This is customer's account information for person1")
#	Bank1.show_customer_accounts(person)
	#print("This is all for person 2customer account information")
#	bank1.add_customer(person2)
#	print(bank1.show_customer_accounts(person2))

	

