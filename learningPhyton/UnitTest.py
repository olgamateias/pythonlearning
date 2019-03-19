'''
Created on 19 Mar 2019

@author: olma
'''
import unittest
from HandleExceptions import HandleExceptions


class Test(unittest.TestCase):


    def testSum(self):
        result = (5,8)
        sum = HandleExceptions().sumNr(result[0], result[1])
        self.assertEqual(sum, 13)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()