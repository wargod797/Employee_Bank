#!/usr/bin/env python
#PyCharm
"""
Created on Sat Nov  2 09:32:57 2019

@author: sridhar
"""
"""Create a class employee with attributes I'd, name, city, salary,age, experience.
 That class should have function "isheoverpaid" and it should return yes if he
 paid more than 3experience100000 (for 1 to 5 years) 2.5*experience *100000 for more than 5 years experience.
 Otherwise it should return no Create class
 bank customer with attributes name, age, salary, amount. Functions credit and debit.
 both functions should take credit or debit amount as int, if invalid input is
 provided then it should ask for valid input for 5 times,
 after that it should break saying u have reached max. Amount of chances, please try afterwards. If input
 amount is valid then amount attribute to be updated accordingly"""

 
# Gobal Variables
name = input("Enter name: ")
city = input("Enter city: ")     
salary = int(input("Enter salary: "))
age = int(input("Enter age: "))
exp = int(input("Enter experience: "))
 
credit = int(input("Enter credit: "))
debit = int(input("Enter debit: "))
amount = int(input("Enter Amount: "))
 
format_output = "#########################################"
 
 
# Customer Class
class Bank:
    # Contructor Method
    def __init__(self, name, city, age, credit, debit, amount):
        self.amount = amount
        self.balance = debit - credit
        print("- Name: " + name)
        print("- city: " + city)
        print("- Age: " + str(age))
        print("- Credit: " + str(credit))
        print("- Debit: " + str(debit))
        print(format_output)
        print("- Balance: " + str(self.balance))
        print(format_output)
        
    def credit(self):
        x=5
        while (x>=1 and x<=5):
            try:
                amt=int(input('enter the amount you want to credit: '))
                self.amount=self.amount+amt
                print(f'account balance is {self.amount}')
                break
            except  ValueError:
                x=x-1
                print(f'please enter the correct amount, chances left {x} ')
        
    def debit(self):
            x=5
            while (x>=1 and x<=5):
                try:
                    amt=int(input('enter how mich amount want to debit: '))
                    if self.amount>=amt:
                        self.amount=self.amount-amt
                        print(f'available amount is: {self.amount}' )
                    else:
                        print('enter the correct amount')
                    break
                except ValueError:
                    x=x-1
                    print(f'please enter the correct amount, chances left {x} ')
 
 
# Employee Class
class Employee:
    # Contructor Method
    def __init__(self, name, city, salary, age, exp):
        self.exp = exp
        self.salary = salary
        print("- Name: " + name)
        print("- city: " + city)
        print("- Age: " + str(age))
        print("- Experience (years): " + str(exp))
        print("- Salary: " + str(salary))
        print(format_output)
 
    # Check Salary Status
    def analyse_results(self):
        status = "Salary Status >> "
        if self.exp < 5:
            if (3 * self.exp * 100000)  < self.salary:
                print(status + "You're overpaid")
            else:
                print(status + "You're NOT overpaid")
        else:
            if (2.5 * self.exp * 100000) < self.salary:
                print(status + "Salary overpaid")
            else:
                print(status + "You're NOT overpaid")
                print(format_output)
 
 
# Create Employee object
print("\n")
print("[+] Searching for employee information...")
print(format_output)
employee = Employee(name, city, salary, age, exp)
employee.analyse_results()
 
# Create Customer object
print("\n")
print("[+] Searching for customer information...")
print(format_output)
customer = Bank(name, city, age, credit, debit, amount)
a=input('you want to 1.Credit or 2.Debit  \n enter 1 or 2 ')
if a=='1':
   customer.credit()
elif a=='2':
    customer.debit()
else :
    print('enter the correct value')