'''
Created on 11 Mar 2019

@author: olma
'''

class Cilindre():
    '''
    classdocs
    '''
    pi = 3.14

    def __init__(self,height=1,radius=1):
        '''
        Constructor
        '''
        self.height = height
        self.radius = radius
    
    def volume(self):
        volume = Cilindre.pi*self.radius**2*self.height
        print(volume)
        return volume
    
    def surface_area(self):
        #2 π r2 + 2 π r h
        area = 2*Cilindre.pi*(self.radius**2) + 2*Cilindre.pi*self.radius*self.height
        print(area)
        return area
        