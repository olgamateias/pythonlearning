'''
Created on 11 Mar 2019

@author: olma
'''
from Animal import Animal

class Dog(Animal): #Dog(Animal) -> this is how to inherit from class Animal
    '''
    classdocs
    '''

    tale = True
    feet = 4
    
    def __init__(self, breed, name, dogAge):
        '''
        Constructor
        '''
        Animal.__init__(self) # this line calls the Constructor from the inherited class Animal
        self.breed = breed
        self.name=name
        self.dogAge = dogAge
    
    def feedDog(self, hungry):
        if(hungry):
            print('the dog is hungry. Feed him')
        else:
            print('the dog is not hungry')
    
    def bark(self, number):
        print('auuuu! my name is {} and a random number {}'.format(self.name, number))
    def swing(self):
        if Dog.tale:
            print('the dog swings his tale. he is happy!')
        else:
            print('the tale is cut off...')
    def who_am_i(self):
        print('i am a dog!')
    def eat(self):
        print('{} is eating'.format(self.name))
    
    #this is a string representation of this class
    def __str__(self):
        return f"{self.name} is {self.dogAge} years old"