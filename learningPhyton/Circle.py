'''
Created on 11 Mar 2019

@author: olma
'''

class Circle():
    '''
    classdocs
    '''
    pi = 3.14

    def __init__(self, radius=1):
        '''
        Constructor
        '''
        self.radius = radius
        self.area = radius**2*Circle.pi
        
    def get_circumference(self):
        return self.radius * Circle.pi * 2    