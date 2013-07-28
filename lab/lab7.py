class Person(object):
    def __init__(self, name):
        self.name = name

    def say(self, stuff): 
    	self.previous = stuff 
    	return stuff

    def ask(self, stuff):
        return self.say("Would you please " + stuff)

    def greet(self):
        return self.say("Hello, my name is " + self.name)

    def repeat(self):
    	return self.say(self.previous)


class Account(object):
    """A bank account that allows deposits and withdrawals."""

    interest = 0.02

    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
        self.transactions = []

    def deposit(self, amount):
        """Increase the account balance by amount and return the new balance."""
       	self.transactions.append(('deposit', amount))
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        """Decrease the account balance by amount and return the new balance."""
       	self.transactions.append(('withdraw', amount))
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        return self.balance

class CheckingAccount(Account):
    """A bank account that charges for withdrawals."""

    withdraw_fee = 1
    interest = 0.01

    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_fee)

    def deposit_check(self, check):
    	if self.holder != check.payable_to or check.deposited:
    		return 'The police have been notified.'
    	else:
	    	self.deposit(check.amount)
	    	check.deposited = True

class Check(object):
	def __init__(self, payable_to, amount):
		self.payable_to = payable_to
		self.amount = amount
		self.deposited = False
