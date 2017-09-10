#! /usr/bin/env/ python3

import sys
import os
from bank_classes.customer_class import Customer
from bank_classes.bank_class import Bank

def prompt():
	print("""1. New Customer
2. Existing Customer
3. Exit""")


def customer_sign_in():
	print("Please select an answer:")
	print("""1. New Customer
2. Existing Customer
3. Exit""")
	while(1):
		answer = input()
		if(answer.isalpha() or int(answer) < 1): 
			print("Incorrect entry, please try again")	
			prompt()			

		elif((int(answer) > 3) and ((int(answer) != 11) and (int(answer) != 22))):
			print("Incorrect entry, please try again")
			prompt()
		else:
			break 
	return(answer)


def home_screen(Bank):
	customer = 1
	name = "" 
	while(customer):
		sign_in = int(customer_sign_in())
		if(sign_in == 3):
			print("Program exitting...")
			sys.exit()
		
		elif(sign_in == 2):
			print("please Enter your name")
			customer = input()
			if customer.isnumeric():
				print("Name contained numbers")
				continue
			for i in Bank.customers:
				if customer == i.name:
					return(customer)
				else:
					customer = 0
		
		elif(sign_in == 1):
			print("Welcome to {}".format(Bank.name))
			person = Customer()
			Bank.add_customer(person)
			print('''If you want to manage accounts please select 2 for existing customer.
Otherwise, press 3 to exit. Thank you.''')

		elif(sign_in == 11):
			print("Company mode add customers for {}".format(Bank.name))
			person = Customer()
			Bank.add_customer(person)
	
		elif(sign_in == 22):
			print("Showing all bank customers and account information")
			print(Bank)
			customer = 0
			name = "zzz"
	
		else:
			print("Enter customer name")
			name = input()
			customer = 0
	return(name)


def menu_choice(name):
	if len(name) < 2:
		print("Invalid name")
		choice = 6
		return choice
	elif name == "zzz":
		choice = 6
		return choice
	print("Hi {}, Welcome to Banc de l'Amerique! What would you like to do?".format(name))
	print("""1. Deposit
2. Withdraw
3. Add account
4. Check balance
5. Change Currency
6. Go back
7. End of Transactions. All Session will close""")
	choice = int(input())
	return(choice)


def menu_choice_execution(Bank, name , choice):
	
	if choice != 6:
		account_type = input("Input account of interest> ")
	if choice == 1:
		bank_deposit(Bank, name, account_type)
	
	elif choice == 2:
		bank_withdrawal(Bank, name, account_type)
		
	elif choice == 3:
		create_account(Bank, name, account_type)	

	elif choice == 4:
		show_balance(Bank, name, account_type)
	
	elif choice == 5:
		print("Skipping this option for now")	
	
	elif choice == 6:
		print("Going to main menu...")
		return(6)

	elif choice == 7:
		print("Exitting program. Thank you.")

	else:
		print("invalid option, please select again")
	return(0)

def bank_deposit(Bank, customer_id, account_type):
	for i in (Bank.customers):
		if customer_id == i.name:
			Bank.deposit(i, account_type)
		else:
			print("Not valid customer")
	return(0)

def bank_withdrawal(Bank, customer_id, account_type):
	for i in (Bank.customers):
		if customer_id == i.name:
			Bank.withdrawal(i, account_type)
		else:
			print("Not valid customer")


def create_account(Bank, customer_id, account_type):
	for i in (Bank.customers):
		if customer_id == i.name:
			i.create_account(account_type)

def show_balance(Bank, customer_id, account_type):
	for i in (Bank.customers):
		if customer_id == i.name:
			print(Bank.get_customer_accounts(i))

	
def mainloop():
	bank1 = Bank("Banc de l'Amerique")		
	customer = 1 
	while(customer):
		transaction = 1
		name = home_screen(bank1)
		while(transaction):
			choice = menu_choice(name)
			result = menu_choice_execution(bank1, name, choice)
			if result == 6:
				transaction = 0
			else:
				print("Do you have any more transactions")
				answer = input("Yes or No")
				os.system('clear')
				if answer.isnumeric():
					print("invalid answer")
				elif answer.lower() == "yes":
					continue
				elif answer.lower() == "no":
					print("Would you like to manage another customer")
					answer = input("Yes or No")
					os.system('clear')
					if answer.lower() == "no":
						print("Program will exit")
						print("exitting")
						sys.exit()
					elif answer.lower() == "yes":
						transaction = 0
					elif answer.isnumeric():
						print("invalid answer, will go to home screen")
						transaction = 0
					else:
						print("invalid answer, going to home screen")
						transaction = 0
				else:
					print("Did not enter yes or no, going to home screen")
					transaction = 0
				os.system('clear')
	
if __name__ == "__main__":
	try:
		mainloop()
	except (KeyboardInterrupt, ValueError) as exception:
		os.system('clear')
		print("Improper attempt to exit. Please exit by either ending session or exitting through interface")
		mainloop()	

	
