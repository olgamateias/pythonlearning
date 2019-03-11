'''
Created on 11 Mar 2019

@author: olma
'''

class Animal():
    '''
    classdocs
    '''
    

    def __init__(self):
        '''
        Constructor
        '''
        print('animal is created!')
    
    def eat(self):
        raise NotImplementedError("Subclass must implement this abstract method")
    
    def who_am_i(self):
        print('i am an animal')