'''
Created on Mar 1, 2019

@author: User
'''
import learningEx
from Dog import Dog
from Circle import Circle
from Line import Line
from Cilindre import Cilindre
from HandleExceptions import HandleExceptions
from Account import Account

if __name__ == '__main__':
    result = learningEx.newFunction(3, 6)
    print(result)
    print(learningEx.dog_check("Dog Year is a wonderful movie"))
    print(learningEx.pig_latin('tree'))
    learningEx.is_prime2(19)
    
    dog = Dog('husky', 'Lissa', 7)

    dog.feedDog(True)
    print(dog.tale)
    print(dog.feet)
    dog.bark(5)
    dog.swing()
    dog.eat() #this is an inherited method
    dog.who_am_i()
    print(dog)
    
    myCircle = Circle(30)
    print(myCircle.area)
    print(myCircle.get_circumference())
    
    coordinate1 = (3,2)
    coordinate2 = (8,10)

    li = Line(coordinate1,coordinate2)
    li.distance()
    li.slope()
    
    c = Cilindre(2,3)
    c.volume()
    c.surface_area()
    #nr1 = HandleExceptions().get_int()
    #nr2 = HandleExceptions().get_int()
    
    #nr2=HandleExceptions.get_int()
    #nr2=int(input("Please add a number "))
    #result = HandleExceptions().sumNr(nr1, nr2) # here, for nr2, the fact that we are requesting a number via input - results a string. # therefore the error "TypeError: sumNr() missing 1 required positional argument: 'nr2'"# we need to cast it 
    
    account1 = Account("Olga", 150)
    account1.deposit(52)
    account1.withdrawl(32)
    account1.withdrawl(232)