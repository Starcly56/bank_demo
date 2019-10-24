import sys
class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
    def deposit(self, damount):
        self.balance = damount
    def withdraw(self, wamount):
        self.balance = wamount
    def quit(self):
        sys.Exit()
print("Welcome to Standard Chartered Bank!!")
print(" Deposit as d \n Withdraw as w \n Exit as e")
customer1 = BankAccount(input("Enter your name: "))
while True:
    operation=input("What do you want?")
    if operation=="b"or operation=="B":
        print("The balance in your account is Rs. "+str(customer1.balance)+" Mr. "+str(customer1.name))
    elif operation=="d" or operation=="D":
        customer1.deposit=int(input("Enter amount to deposit: "))
        print("Total balance in your account is Rs. "+str(customer1.balance+customer1.deposit))
        customer1.balance=customer1.balance+customer1.deposit
    elif operation=="w" or operation=="W":
        customer1.withdraw=int(input("Enter amount to withdraw: "))
        if customer1.balance<customer1.withdraw:
            print("Insufficient balance."+" You have "+str(customer1.balance)+" balance.")
        else:
            print("Total balance in your account is Rs. "+str(customer1.balance - customer1.withdraw))
            customer1.balance=customer1.balance-customer1.withdraw
    elif operation=="e"or operation=="E":
        sys.exit()
    else:
        print("Invalid operation!!!!!!!!!")

