'''
Created on 1 Apr 2019

@author: olma
'''

class Account():
    '''
    classdocs
    '''


    def __init__(self, owner, balance):
        '''
        Constructor
        '''
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        print('Your account was debited with {} $. Your current balance is {} $'.format(amount, self.balance))
    
    def withdrawl(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("You have withdraw {} $. Your current balance is {} $".format(amount, self.balance))
        else:
            print("Unavailable funds. You are trying to withdraw a bigger amount then your balance.")
        