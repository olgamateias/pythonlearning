'''
Created on 11 Mar 2019

@author: olma
'''
import math

class Line():
    '''
    classdocs
    '''


    def __init__(self, coor1, coor2):
        '''
        Constructor
        '''
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        # distance = radical din (x2-x1) la patrat + (y2 -y1) la patrat
        # x1, y1 = self.coor1
        # x2, y2 = self.coor2
        distance = math.sqrt((self.coor2[0]-self.coor1[0])**2 + (self.coor2[1] - self.coor1[1])**2)
        print(distance)
        return distance
    
    def slope(self):
        m = (self.coor2[1] - self.coor1[1]) / (self.coor2[0]-self.coor1[0])
        print(m)
        return m
        