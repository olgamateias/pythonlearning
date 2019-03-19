'''
Created on 19 Mar 2019

@author: olma
'''

class HandleExceptions():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''

    def sumNr(self, nr1, nr2):
        print(nr1+nr2)
        return nr1+nr2
    
    def get_int(self):
        while True:
            try:
                result = int(input("Handle exceptions class. Please enter a number "))
            except:
                print("You did not entered a number. Please try again.")
            else:
                print(str(result) + " is a valid number")
                break
            finally:
                print("End of method.")
        return result