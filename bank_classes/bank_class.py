#! /usr/bin/env python3

from decimal import Decimal
from bank_classes.customer_class import Customer




class Bank():

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

	
		

	def __str__(self):
		result = ""
		print("*" * 30)
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


