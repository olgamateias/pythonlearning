from operator import index
import math
from collections import Counter
from collections import defaultdict
from collections import OrderedDict
from collections import namedtuple
import datetime
from _datetime import tzinfo
import timeit
import re 
import io
from io import StringIO
from ipywidgets import  interact, interactive, fixed
import ipywidgets as widgets


print('Hello, Olga')
print('yes - another Hello, World!')
print(2+1)

print(2+5)
print(3/2)
print(7%4)
print(2**3) #2 la puterea a 3a
my_income = 300

tax_rate = 0.15
tax_value = my_income * tax_rate
print(tax_value)
newStr = "Hellom"
second = "Olga"
print(newStr + ", "+second)
print(newStr.index("o"))#index of letter o -> 4, from Hello
print(newStr[4])#return letter that is at index 4 -> o
print(newStr[-1])#reverse index -1 is associated with the last letter/index if the word becomes Hellom => -1 will return "m" and not o
print("teste \ntest")# \n is for new line
print("teste \ttest")# \n is for TAB
print(len(newStr))#length of a string
testString = "abcdefghijk"
print(testString[2:])#substring from char at index 2 untill end
print(testString[:3])#substr from the begining until index 3, not including index 3
print(testString[2:6])#substring from index 2 until, not including, index 6
print(testString[::2])#substring from index 0 until the end, but jumping from 0 +2 elements => acegik
print(testString[::3])#substring from index 0 until the end, but jumping from 0 +3 elements => adgj
print(testString[2:7:2])#substring from index 2 until index 7, but jumping from 2 +2 elements => ceg
print(testString[::-1])#reverse string
anotherString = 'Z' + newStr[1:]#cancat 2 strings
print(anotherString)
s = "Hi this is a string"
print(s.split()) #the split() made by space 9default) and returns a list
print(s.split("i")) #splits the string s by letter i
print("this is new {}".format("inserted")) #string format
print("The {} {} {}".format("fox", "brown", "quick"))
print("The {2} {1} {0}".format("fox", "brown", "quick"))
print("The {2} {2} {2}".format("fox", "brown", "quick"))
print("The {q} {b} {f}".format(f="fox", b="brown", q="quick"))
result = 100/777
print("The result was {r}".format(r=result))
print("The result is {r:1.3f}".format(r=result)) #formats the width and decimals after comma
name = "Jose"
print("Hello, {}".format(name))
print(f"Hello, {name}") #same thing different
age=5
print(f"{name} is {age} years old")
my_list = [1,2,3]
new_list = ["string", 100, 23.53] #lists in python can hold different obj types
my_list = ["one", "two", "three"]
y_list = ["four", "five", "six"]
new_list = my_list + y_list #concat lists
print(new_list)
print(new_list[4])
print(new_list[2:4]) #slicing
new_list[0] = new_list[0].upper()
new_list.append("seven") #add item to the list
new_list.append("eight") #add item to the list
new_list.pop() #removes the last object from the list
popped_el = new_list.pop(1) #removes the element that is at index 1 from the list and the removed el can be saved
print(new_list)
print(popped_el)
string_list = ["a", "z", "o","b"]
num_list = [8,5,1,0,9]
string_list.sort()
num_list.sort() #doesn't return anything -> this can't be assigned to another list
nr_new_list = num_list
print(string_list)
print(num_list)
print(nr_new_list)
nr_new_list.reverse()
print(nr_new_list)
nested_list = [1,1,[1,2]]
print(nested_list[2][1])
list1=[1,2,3]
list2=[4,5,6]
list3=[7,8,9]
matrix=[list1,list2,list3]
print(matrix[1])
print(matrix[1][2])
first_col = [row[0] for row in matrix] #to grab the first element of every row in the matrix object
print(first_col)

my_dict = {'key1':'value1', 'key2':'value2', 'key3':'value3'}
print(my_dict['key3'])
my_dict={'apple': 1.99, 'oranges':0.89, 'avocado':1.29}
print(my_dict['apple'])
my_dict={'k1':123, 'key2':[1,2,3], 'key3':{'insideKey1':11.99, 'insideKey2':15.99}}
print(my_dict['key2']) #return the value for key2, which is a list
print(my_dict['key2'][1]) #return the value that has index 1 in the list, which is the value for key2
print(my_dict['key3']['insideKey2']) #the value for key3 is a dictionary 
my_TupleList = (1,2,'new') #tuples is an Immutable list, like an array in Java
#my_TupleList[2] = 3 #TypeError: 'tuple' object does not support item assignment

listNew = [3,3,3,5,5,2,2,1,1,]
mySet = set(listNew) #Sets are an unordered collection of unique elements. We can construct them by using the set() function.
print(mySet)
mySet.add(6)
print(mySet)
False #with capital first letter
True #with capital first letter
print(1>2)
print(1==1)
b=None ##null in Java

"""
For Windows you need to use double \ so python doesn't treat the second \ as an escape character, a file path is in the form:

myfile = open("C:\\Users\\YourUserName\\Home\\Folder\\myfile.txt")
For MacOS and Linux you use slashes in the opposite direction:

myfile = open("/Users/YouUserName/Folder/myfile.txt")

my_file = open("/Users/olma/Downloads/Olga's folder/python_wrk/Complete-Python-3-Bootcamp-master/00-Python Object and Data Structure Basics/test.txt")
print(my_file.read()) # returns the content from the file as a string
my_file.seek(0) #resets the cursor to initial position, otherwise, the next command will return empty string/ list, because the cursor is at the end of text/file and there is nothing :) 
print(my_file.readlines()) # returns the content from the file as a list with strings
my_file.close() #the file needs to be close
#OR
#you can open it with 'with' statement (remember with in sql?)
with open("/Users/olma/Downloads/Olga's folder/python_wrk/Complete-Python-3-Bootcamp-master/00-Python Object and Data Structure Basics/test.txt") as myNewFile:
    content = myNewFile.read()
    print("with and content \n"+content)
"""
"""
mode='r' is read only
mode='w' is write (will overwrite files or create new ones
mode='a' is append only (will add on to files)
mode='r+' is reading and writing
mode='w+' is writing and reading (overwrites the existing files or creates a new one!)
"""
"""
with open("/Users/olma/Downloads/Olga's folder/python_wrk/Complete-Python-3-Bootcamp-master/00-Python Object and Data Structure Basics/new_file.txt", mode='w') as f:
    content = f.write("some text as example")

with open("/Users/olma/Downloads/Olga's folder/python_wrk/Complete-Python-3-Bootcamp-master/00-Python Object and Data Structure Basics/new_file.txt", mode='r') as f:
    content = f.read()
    print("example: " +content)

with open("/Users/olma/Downloads/Olga's folder/python_wrk/Complete-Python-3-Bootcamp-master/00-Python Object and Data Structure Basics/new_file.txt", mode='a') as f:
    content = f.write("\nnew line")
    
with open("/Users/olma/Downloads/Olga's folder/python_wrk/Complete-Python-3-Bootcamp-master/00-Python Object and Data Structure Basics/new_file.txt", mode='r') as f:
    content = f.read()
    print("a mode means adding text in file. \nadded text: " +content)
"""
#comparision
print(1<2<3)
print(1<2 and 2<3)
print(1<2 and 2>3)
print(100 ==1 or 2==2)
print(not(1==1))
print(not(400>5000))
x=25
if(x>23):
    print("greater then 23")
else: 
    print("smaller or equal to 23")

score = 3000
if(score >= 1 and score <= 1000):
    print("level 1")
elif(score >=1001 and score <= 2000):
    print("level 2")
elif(score >= 2001 and score <= 3000):
    print("level 3")
else:
    print("level 0")

my_list = [3,5,7,9,0,1,2,4,6,8]
for nr in my_list:
    if (nr%2==0):
        print("even nr " + str(nr))
    elif(nr%2 !=0):
        print("odd nr " + str(nr))
list_sum=0
for number in my_list:
    list_sum = list_sum + number
print("list sum is " + str(list_sum))

myString= "hello world"
for letter in myString:
    print(letter)

myList = [(1,2),(3,4),(5,6)]

#first going through list
for item in myList:
    print(item)

#second going through tuples from the list
for (a,b) in myList:
    print(a)
    print(b)

#second going through tuples from the list
for a in myList:
    print(a[0])
    
#for loop for dictionaries
d={'key1':1,'key2':5,'key3':9}
#go through keys
for item in d: #or d.keys()
    print(item)

#gothrough values
for item in d.values():
    print(item)
    
#go through values or keys
for k,v in d.items():
    print(v)

print(234%100)
print(201//100)

year = 200
century=0
if(year%100 > 0):
    century = year//100 +1
else:
    century = year//100
print("century " + str(century))    

#palindrom
def checkPalindrome(inputString):
    isPalindrome= False
    i=-1
    count=0
    for letter in inputString//2:
        if(letter == inputString[i]):
            count=+1
            i-=1
    

    return isPalindrome   

for index, item in enumerate(testString):
    print(index, item)

testString = 'zzzazzazz'

i=-1
isPalindrome= False
for index in range(len(testString)//2):

    print(index, testString[index])
    if(testString[index] == testString[i]):
        
        isPalindrome = True
        i-=1
    else:
        isPalindrome=False
        i-=1
        
    print(isPalindrome)

#while loop
x=0
while(x<5):
    print(f'the current value of x is {x}')
    x+=1
else:
    print("x is not less than 5")     

# break
# continue
# pass - does nothing

#range
z=[1,2,3,4,5,6]
print(len(z))
for num in range(len(z)//2): #range here is used to iterate just through half of the list
    print(f'half z array {z[num]}')
print()
for num in range(0,11,2):#start at 0 in the list, iterate until, but not including, 11, jump 2 steps (din 2 in 2)
    print(num)

index_count=0
word = 'abcdef'
for letter in word:
    print('At index {} the letter is {}'.format(index_count, letter))
    #OR
    print(word[index_count]) #prints just the letter, without the index
    index_count +=1

#enumerate
word = 'abcdef'
for item in enumerate(word):
    print(item) #prints Tuples = (index, value) 
    #-> thereforewe can write the for like this
for item, letter in enumerate(word):
    print(item)
    print(letter)
    print()

# zip
myList1 = [1,2,3,4,5]
myList2 = ['a','b','c']
myList3 = [11,22,33]
print(list(zip(myList1, myList2, myList3))) #so zip excludes the extra values, if they do not have a correspondent
for item in zip(myList1,myList2):
    print(item)
for first, second, third in zip(myList1,myList2, myList3):#therefor we can unpack 
    print(first)
    print(second)
    print(third)

# in
print('a' in 'mamass')
print('myKey' in {'myKey1' : 'value1', 'yourkey':'value2'})
d={'myKey1' : 'value1', 'yourkey':'value2'}
print('value1' in d.values())

#min and max
newlist = [8,43,12,89,111]
print(min(newlist))
print(max(newlist))

#read input from user
#name = input('Enter your name: ')
#age = input('Enter your age: ') #is a string
#print(f'{name} is {age} years old')

# List comprehensions
listComprehension = [letter for letter in 'hello']
print(listComprehension) 
#the above is exactly the below standard code, but in one line
listCompr = []
for letter in 'hello':
    listCompr.append(letter)
print(listCompr)

#another ex with math operations
numList = [num**2 for num in range(0,11)]
print(numList)
#which is equivalent to:
numList = []
for num in range(0,11):
    numList.append(num**2)
print(numList)

#another ex with IF
myList = [num for num in range(0,11) if num%2==0]
print(myList)

myList =[]
for num in range(0,11):
    if(num%2 == 0):
        myList.append(num)
print(myList)

#another ex with IF ELSE
myList = [x if x%2==0 else 'ODD' for x in range(0,11)]
print(myList)

#ex with 2 FOR loops
myList=[x*z for x in [2,4,6] for z in [1,10,100]]
print(myList)

myList=[]
for x in [2,4,6]:
    for z in [1,10,100]:
        myList.append(x*z)
print(myList)


def newFunction(num1, num2):
    return num1+num2

def dog_check(myString):
    return 'dog' in myString.lower()

def pig_latin(word):
    first_letter = word[0].lower()
    #check if first_letter is a vowel
    if first_letter in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + first_letter + 'ay'
    return pig_word
rangeList = range(2,16)
print(rangeList)

def is_prime2(num):
    '''
    Better method of checking for primes. 
    '''
    #because even numbers, except 2, are not prime
    if num % 2 == 0 and num > 2: 
        return False
    #all prime numbers are odd, that's why we start from 3 and jump 2 numbers
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

print(int(math.sqrt(19))+1)

# *args is something like *=all in SQL
def myfunc(*args):
    return sum(args) * 0.05 #the sum of all arguments received * 5%
print(myfunc(40,60,100))
# this is when you expect many arguments passed into the function
# So... instead of this
def newFunc(a,b,c=0,d=0,e=0):
    return sum(a,b,c,d,e) * 0.05
print(myfunc(40,60,100, 100))
# python accepts this *args (args can be something else, like 'param', the important thing is the star *)
def paramfunc(*param):
    return sum(param) * 0.05 #the sum of all arguments received * 5%
print(paramfunc(20,50,120))

# args are a Tuple, so you can iterate through them
def tupFunc(*args):
    for item in args:
        print(item)
tupFunc(12,23,45,56,98)

# another alternative is **kwargs = key words args -> creates a dictionary
def kwFunc(**kwargs):
    if 'fruit' in kwargs:
        print('I choose {}'.format(kwargs['fruit']))
    elif 'nuts' in kwargs:
        print('I want {} today'.format(kwargs['nuts']))
    else:
        print('I do not want any fruits. Maybe a {} to cook.'.format(kwargs['veggie']))
kwFunc(fruit='apple', veggie = 'potato', nuts='almonds')
kwFunc(dairy='milk', veggie = 'potato', nuts='almonds')
kwFunc(dairy='milk', veggie = 'potato', tea='black')

#this two can be combined
def combinedFunc(*args, **kwargs):
    print(args)
    print(kwargs)
    print('I need to buy {} {} '.format(args[2], kwargs['drink']))
combinedFunc(1,2,3,4,5, fruit='apple', dairy = 'milk', drink='beer', sweets='choco', cake='napoleon')

#challenge
def strfunc(inputString):
    newString=''
    for i in range(1, len(inputString)+1):
        if(i%2==0):
            newString=newString+inputString[i-1].upper()
        else:
            newString=newString+inputString[i-1].lower()
    return newString
print(strfunc('Anthropomorphism'))

'''LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd
lesser_of_two_evens(2,4) --> 2
lesser_of_two_evens(2,5) --> 5
'''
def lesserOfTwoEvens(a,b):
    if a%2==0 and b%2==0:
        print(min(a,b))
        return min(a,b)
    else:
        print(max(a,b))
        return max(a,b)
lesserOfTwoEvens(8, 2)

def animalCrackers(string):
    myList=string.split()
    for item in range(0, len(myList)):
        for nextItem in range(1, len(myList)):
            print(myList[item][0] )
            print(myList[nextItem][0])
            if myList[item][0] == myList[nextItem][0]:
                print(True)
                return True
            else:
                print(False)
                return False
animalCrackers('String Otring')

def makes_twenty(n1,n2):
    return (n1+n2==20) or (n1==20) or (n2==20)
'''   
    if (n1+n2==20) or (n1==20) or (n2==20):
        print(True)
        return True
    else:
        print(False)'''
    
makes_twenty(2, 8)

''' Write a function that capitalizes the first and fourth letters of a name '''
def old_macdonald(name):
    newString = name[:3].capitalize() + name[3:].capitalize()
    print(newString)
    return newString
old_macdonald('macdonald')

''' Given a sentence, return a sentence with the words reversed
master_yoda('I am home') --> 'home am I'
master_yoda('We are ready') --> 'ready are We' '''
def master_yoda(text):
    list=text.split()
    print(list)
    newString=''
    #the long way, without ::-1
    
    for item in range(len(list)-1, -1, -1):
        if(item == len(list)-1):
            newString=list[item]
        else:
            newString=newString+' '+list[item]
    print(newString)
    return newString
#the short way
''' newList = list[::-1]
    newString = ' '.join(newList) -> joins the elements from the list with space between them
    print(newString)
    return newString'''
master_yoda('I am home')

''' FIND 33:
Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

has_33([1, 3, 3]) → True
has_33([1, 3, 1, 3]) → False
has_33([3, 1, 3]) → False'''
def has_33(num):
    for item in range(0, len(num)-1):
        if num[item] == 3 and num[item+1]==3:
            print(True)
            return True
    print(False)
    return False

has_33([1,3,3])

'''Given a string, return a string where for every character in the original there are three characters
paper_doll('Hello') --> 'HHHeeellllllooo'
paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii' '''
def paper_doll(text):
    newString=''
    for letter in text:
        newString=newString+(letter*3)    
    print(newString)
    return newString
paper_doll('Hello')

''' Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. 
If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. 
Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
blackjack(5,6,7) --> 18
blackjack(9,9,9) --> 'BUST'
blackjack(9,9,11) --> 19'''
def blackjack(a,b,c):
    sum=a+b+c
    
    if(a==11 or b==11 or c==11):
        sum=sum-10
    
    if sum > 21:
        print('BUST')
        return 'BUST'      
    
    print(sum)    
    return sum
blackjack(9,9,11)

''' Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
summer_69([1, 3, 5]) --> 9
summer_69([4, 5, 6, 7, 8, 9]) --> 9
summer_69([2, 1, 6, 9, 11]) --> 14 '''
def summer_69(arr):
    indexSix = arr.index(6)
    indexNine = arr.index(9)
    sum=0
    firstList=arr[:indexSix]
    print(firstList)
    if(indexNine < len(arr)-1):
        secondList=arr[indexNine+1:]
    else:
        secondList=[]
        print(secondList)
    for item in firstList+ secondList:
        sum=sum+item
    print(sum)
    return sum
summer_69([4,5,6,7,8,9])
# [4,5,6,7,8,9,4,5,6,7,8,9] try with this ex
'''Write a function that takes in a list of integers and returns True if it contains 007 in order
 spy_game([1,2,4,0,0,7,5]) --> True
 spy_game([1,0,2,4,0,5,7]) --> True
 spy_game([1,7,2,0,4,5,0]) --> False '''
def spy_game(nums):
    newStr=''
    for num in nums:
        if num == 0 or num == 7:
            newStr=newStr+str(num)
    print(newStr)
    if newStr == '007':
        print(True)
        return True
    print(False)
    return False
spy_game([1,7,2,0,4,5,0])
    
''' Write a function that returns the number of prime numbers that exist up to and including a given number
count_primes(100) --> 25
By convention, 0 and 1 are not prime. '''
def count_primes(num): 
    count=1
#    oddList=range(3, num, 2)
 #   print(oddList)
    for int in range(3, num, 2):
        if int == 3 or int ==5 or int ==7:
            count+=1
        elif int%3!=0 and int%5!=0 and int%7!=0 :
            count+=1   
    print(count)
count_primes(100)

print(abs(100-104))


# map function map(func, *iterables) --> map object: receives a function and a iterable object (list, dict, tuples, etc)
def square(num):
    return num**2
my_nums = [1,2,3,4,5]
print(list(map(square, my_nums)))

def evenString(my_string):
    if len(my_string)%2==0:
        return 'even string'
    else:
        return len(my_string)
some_strings=['Andy', 'Mickael', 'Trotski', 'Agatha']
print(list(map(evenString,some_strings)))

# filter function map(func, *iterables) --> map object
def check_even(num):
    return num%2==0
my_nums=[13,2,8,7,5,11,12]
print(list(filter(check_even,my_nums)))

# LAMBDA expression -> lambda expressions allow us to create "anonymous" functions. This basically means we can quickly make ad-hoc functions without needing to properly define a function using def.
print(list(map(lambda num: num**2, my_nums)))
print(list(filter(lambda item: item%2==0, my_nums)))
print(list(filter(lambda item: len(item)%2==0, some_strings)))
print(list(map(lambda item: item[::-1], some_strings)))
print(list(map(lambda item: item[0], some_strings)))

#local, enclosed or global
''' LEGB Rule:

L: Local — Names assigned in any way within a function (def or lambda), and not declared global in that function.

E: Enclosing function locals — Names in the local scope of any and all enclosing functions (def or lambda), from inner to outer.

G: Global (module) — Names assigned at the top-level of a module file, or declared global in a def within the file.

B: Built-in (Python) — Names preassigned in the built-in names module : open, range, SyntaxError,...
'''

name='is a global string var'

def greet():
    #name = 'is an enclosed funct local var'
    
    def gello():
        #name = 'is a local var'
        print('var <name> ' + name)
    gello()

greet()

#scope of variables
x=50
def func():
    global x #in this way you are calling the global var (x=50) in this function and here you can reassign it
    print(f'global variable X {x}')
    x='new value'
    print(f'global variable was changed/ reassigned to {x}')
func()
print(x) # you will notice here that the value of the global variable has changed
# changing the global variables is not always a very good idea. Instead we can do this:

def func2(x):
    print(f'global variable X {x}')
    x='i am local now'
    print(f'global variable was changed/ reassigned to {x}')
    return x
x=func2(x)
print(x)

nr1=10
#nr2=input("Please enter a number ") #TypeError: unsupported operand type(s) for +: 'int' and 'str'

#nr2=int(input("Please enter a number ")) # but - this will not handle the cases when the user will enter letters
'''
def get_int():
    while True:
        try:
            result = int(input("Please enter a number "))
        except:
            print("You did not entered a number. Please try again.")
        else:
            print(str(result) + " is a valid number")
            break
        finally:
            print("End of method.")
    return result
nr2=get_int()  
nr3=get_int()  
def addValues(nr1, nr2):
    print(nr1+nr2)
addValues(nr3, nr2)
'''

def testfunct():
    #print("hi!")
    return 4
testfunct()
testVar = testfunct() #you can assign a function to a variable
print(testVar)
del testfunct
#print(testfunct()) #NameError: name 'testfunct' is not defined
print(testVar)

def firstFunction(nr):
    
    def secondFunct():
        print("this is the secondFunction() created in another function (firstFunction).")
        return 8
    def thirdFunction():
        print("this is the thirdFunction() created in another function (firstFunction).")
        return 1
    if nr == 8:
        return secondFunct()
    elif nr == 1:
        return thirdFunction()
    else:
        return nr
print(firstFunction(8))

def newTestFunction():
    return "New function"
def other(some_funct_name):
    print("this function can execute the code from another function")
    print(some_funct_name())
other(newTestFunction)

def new_decorator(original_funct):
    def wrap_funct():
        print("\t some extra code, before the original function")
        
        original_funct()
        
        print("\t some extra code, after the original function")
    return wrap_funct

def funct_needs_decorator():
    print("i want to be decorated!")

# one way of doing it
decorated_func = new_decorator(funct_needs_decorator)
decorated_func()
print('-----------------------------------')
#another way of doing it
@new_decorator
def another_funct_needs_decorator():
    print('another way of decorating a function')
another_funct_needs_decorator()

print('-----------------------------------')
# generate a range of numbers: 1 way
def create_cubes(n):
    result = []
    for x in range(n):
        result.append(x**3)
    return result
print(create_cubes(10))
for x in create_cubes(10):
    print(x)

# generate a range of numbers: another way
def created_cubes2(n):
    for x in range(n):
        yield x**3
print(created_cubes2(10))
print(list(created_cubes2(11)))

for y in created_cubes2(11):
    print(y)
print('-----------------------------------')

#generate fibonacci array
def gen_fibon(n):
    a=1
    b=1
    for i in range(n):
        yield a
        a,b = b,a+b

for z in gen_fibon(10):
    print(z)

print('-----------------------------------')
g=gen_fibon(9)

print(next(g))
print(next(g))
print(next(g))
print('-----------------------------------')
newString = "hello"
s_iter=iter(newString)
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print('-----------------------------------')
l = [1,1,1,32,12,12,32,4,5,6,4,5,6,2,2,2]
print(Counter(l))
randomWord="asssbbvvaacdecde"
print(Counter(randomWord))

textW = "how many times have times and how many words have words"
listWords = textW.split()
print(Counter(listWords))
counterVar = Counter(listWords)
print(counterVar.most_common())
print(sum(counterVar.values()))
print(list(counterVar))
print(set(counterVar))
print(dict(counterVar))
list_of_pairs = counterVar.items()
print(list_of_pairs)
print(counterVar.items())
print(Counter(dict(list_of_pairs)))
print(counterVar.most_common()[:-1-1:-1])
counterVar += Counter()
print(counterVar)
print(counterVar.clear())
print('-----------------------------------')
d = defaultdict(object)
d['one'] #now we have a dictionary with a key that does not have a value
print(d)
newD=defaultdict(lambda: 0) #lambda expression will assign for each key value 0, if we do not specify it otherwise
newD['one']
newD['two'] = 2
newD['three']
newD['for']=4
print(newD)
print('-----------------------------------')
#normal dictionaries do not keep the order, even though here they are ordered here
normDict = {}
normDict['a']=1
normDict['b']=2
normDict['c']=3
normDict['d']=4
normDict['e']=5
print(normDict)
for k,v in normDict.items():
    print(k,v)
print('-------------------')
orderedDict = OrderedDict()
orderedDict['a']=1
orderedDict['b']=2
orderedDict['c']=3
orderedDict['d']=4
orderedDict['e']=5
for k,v in orderedDict.items():
    print(k,v)
print('-------------------')
d1={}
d1['a']=1
d1['b']=2
d2={}
d2['b']=2
d2['a']=1
print(d1==d2)  
print('-------------------')
d1=OrderedDict()
d1['a']=1
d1['b']=2
d2=OrderedDict()
d2['b']=2
d2['a']=1
print(d1==d2)  
print('-----------------------------------')
#namedtuple() - creates a tuples which looks like an object, a class
Dog = namedtuple('Dog', 'age name breed hungry')
lissa = Dog(6, 'Lissa', 'husky', True)
print(lissa)
print(lissa.age)
Cat = namedtuple('Cat', 'age name breed hungry')
kissa = Cat(3, 'Kissa', 'european', False)
print(kissa)
print(kissa.hungry)
print('-----------------------------------')
t = datetime.time(15,25,1)
print(t)
print(t.hour)
print(t.minute)
print(t.second)
print(t.tzinfo)
print('------------------')
today = datetime.date.today()
print(today)
print(today.year)
print(today.month)
print(today.day)
print(today.timetuple())
print(datetime.date.today().weekday())
tt=today.timetuple()
print(tt.tm_yday)
yesterday=today.replace(day=24)
print(yesterday)
lastYearToday=today.replace(year=2018)
print(lastYearToday)
print(today-lastYearToday)
print('------timeIT-------------------------')
def costly_func():
   return map(lambda x: x^2, range(10))
print(timeit.timeit(costly_func))

#decorator
def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped
number = 10
wrapped = wrapper(gen_fibon, number)
print(timeit.timeit(wrapped))
print('-----------------------------------')
split_term = '@'
phrase = 'blablalba@gmail.com' #an alternative to extract email username and domain
print(re.split(split_term, phrase))
print('-----------------')
split_term = '/'
phrase = 'AMERICAS GEO/USPS/USPS HQ' #an alternative to extract email username and domain
print(re.split(split_term, phrase))
print('-----------------------------------')
backslash= r'\\' #"\\\\" #r'\\'
patterns = [backslash,":",";"]
textPatt='AMRICAS GEO/SOME-TEXT: REGION\AREA/CITY'
for elem in patterns:
    print('Searching for {} in: {}"'.format(elem, textPatt))
    #check for match
    if re.search(elem, textPatt, flags=0):
        newString=textPatt.replace("\\", "+")
        print(newString)
        print(re.split(elem, textPatt))
        print('match was found')
    else:
        print('no match was found')
print('-----------------------------------')

def multi_re_find(patterns,phrase):
    '''
    Takes in a list of regex patterns
    Prints a list of all matches
    '''
    for pattern in patterns:
        print('Searching the phrase using the re check: %r' %(pattern))
        print(re.findall(pattern,phrase))
        print('\n')

test_phrase = 'sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'

test_patterns = [ 'sd*',     # s followed by zero or more d's
                'sd+',          # s followed by one or more d's
                'sd?',          # s followed by zero or one d's
                'sd{3}',        # s followed by three d's
                'sd{2,3}',      # s followed by two to three d's
                ]

multi_re_find(test_patterns,test_phrase)
print('-----------------------------------')
test_phrase = 'sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'

test_patterns = ['[sd]',    # either s or d
                's[sd]+']   # s followed by one or more s or d

multi_re_find(test_patterns,test_phrase)
print('-----------------------------------')
test_phrase = 'This is a string! But it has punctuation. How can we remove it?'
print(re.findall('[^!.?]+', test_phrase))
print('-----------------------------------')

test_phrase = 'This is an example sentence. Lets see if we can find some letters.'

test_patterns=['[a-z]+',      # sequences of lower case letters
               '[A-Z]+',      # sequences of upper case letters
               '[a-zA-Z]+',   # sequences of lower or upper case letters
               '[A-Z][a-z]+'] # one upper case letter followed by lower case letters
                
multi_re_find(test_patterns,test_phrase)
print('-----------------------------------')
test_phrase = 'This is a string with some numbers 1233 and a symbol #hashtag'

test_patterns=[ r'\d+', # sequence of digits
                r'\D+', # sequence of non-digits
                r'\s+', # sequence of whitespace
                r'\S+', # sequence of non-whitespace
                r'\w+', # alphanumeric characters
                r'\W+', # non-alphanumeric
                ]

multi_re_find(test_patterns,test_phrase)
print('-----------------------------------')
message = 'Imagine here is a long text, maybe a text from web, extracted, that you want to use in your app.'
f = io.StringIO(message)
print(f.read())
f.write(' Another phrase added to the message.')
f.seek(0) #Reset cursor just like you would a file
print(f.read())
f.close()
print('-----------------------------------')
#hexadecimal representation
print(hex(1234))
print(hex(512))
print('--------------')
#binary representation
print(bin(512))
print(bin(128))
print('-----------------------------------')
#other built-in Math functions
print(pow(2,4)) # == 2**4
print(abs(-52))
print(abs(12))
print(round(3.1))
print(round(3.9))
print(round(3.141592, 3))
print('-----------------------------------')
#other built-in String functions
string = 'Dude, where\'s my car'
print(string.count('d')) #counts only lower case 'd'
print(string.count('e'))
print('index of d is ' + str(string.find('d')))
print('index of w is ' + str(string.find('w')))

print(string.isalpha()) #returns false if is a text with spaces or other symbols
print(string.isalnum()) #returns false if is a text with spaces or other symbols
print(string.isascii()) #takes in consideration the spaces and the other symbols
print('------------')
string = 'Hello'
print(string.endswith('o')) 
print(string[-1]=='o')
print(string.istitle())
print('------------')
string='hihhhiihhhhiihh'
print(string.split('i'))
print(string.partition('i')) #('h' = the head, 'i' = the separator, 'hhhiihhhhiihh' = the tail)
print('-----------------------------------')
# some extras for set()
newSet = {1,2,3}
sCopy = newSet.copy()
newSet.add(4)
print(newSet)
print(sCopy)
print(newSet.difference(sCopy))
print(newSet)
#print(newSet.difference_update(sCopy)) #updates the set1 with the result from this operations. The result is {4}, therefore set1 = {4}... this is depricated since python 2.6
print('-----symmetric_difference----')
set1={1,2,3}
set2={1,4,5}
print(set1.symmetric_difference(set2)) #returns a new set {2, 3, 4, 5}
set1={1,2,3}
set2={1,2,5}
print(set1.intersection(set2))
set1={1,2,3}
set2={1,2,3,5}
set3={9,0,8}
print('-----is subset or master set----')
print(set1.issubset(set2))
print(set2.issuperset(set1))
print('-----is disjoint----')
print(set1.isdisjoint(set2))
print(set1.isdisjoint(set3))
print('-----union----')
set4 = set1.union(set3)
print(set4)
print('-----update----')
set5={1,1,1}
set6 = {3,3,0}
set7 = set5.update(set6)
print(set5)
print('-----------------------------------')
#extras for lists
list1=[1,2,3]
list1.append([4,5]) #[1, 2, 3, [4, 5]]
print(list1)
list2=[6,7,8]
list2.extend([4,5])
print(list2)
print('-----insert----')
print(list2)
list2.insert(2, 'inserted') #notice that this insert will not overwrite the value at index 2, but it will shift the values
print(list2)
print('-----------------------------------')
#something new!!!
def interactFunc(x):
    return x+12
print(interact(interactFunc, x=23))
print('-----------------------------------')
#homework
st = 'Print only the words that start with s in this sentence'

for element in st.split():
    if element[0].lower() == 's':
        print(element)
####
#Use range() to print all the even numbers from 0 to 10.
for item in range(0,11,2):
    print(item)

###Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
listCompr = [item for item in range(0,51) if item%3==0]
print(listCompr)

#####
st = 'Print every word in this sentence that has an even number of letters'
list = st.split()
for word in list:
    if len(word)%2==0:
        print(word)
#### Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
for nr in range(0, 101):
    if (nr%3==0) and (nr%5==0):
        print('FizzBuzz')
    elif nr%3==0:
        print('Fizz')
    elif nr%5==0:
        print('Buzz')
    else:
        print(nr)

####
st = 'Create a list of the first letters of every word in this string'
listCompr = [letter[0] for letter in st.split()]
print(listCompr)

####Volume of a sphere
def vol(rad):
    volumeSphere=(4/3)*3.14*(rad**3)
    print(volumeSphere)
    return volumeSphere
vol(2)

#Write a function that checks whether a number is in a given range (inclusive of high and low)

def ran_check(num,low,high):
    if num>=low and num<=high:
        print('{} is in the range between {} and {}'.format(num,low, high)) 
        return True
    print('False')
    return False
ran_check(2, 5, 7)

# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
'''
Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
Expected Output : 
No. of Upper case characters : 4
No. of Lower case Characters : 33

HINT: Two string methods that might prove useful: .isupper() and .islower()

If you feel ambitious, explore the Collections module to solve this problem!
'''
def up_low(s):
    countUp=0
    countLow=0
    print(s.split())
    for word in s.split():
        for letter in word:
            if letter.isupper():
                countUp+=1
            elif letter.isalpha():
                countLow+=1
    print(countUp)
    print(countLow)
s='Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)

# Write a Python function that takes a list and returns a new list with unique elements of the first list.
sampleList = [1,1,1,1,2,2,3,3,3,3,4,5]
uniqlist=[sampleList[0]]
print(uniqlist)
for item in sampleList:
    if item not in uniqlist:
        uniqlist.append(item)
print(uniqlist)

#Write a Python function to multiply all the numbers in a list.

def multiply(numbers):
    result=1
    for item in numbers:
        result = result*item
    print(result)
    return result
multiply([1,2,3,-4])

#Write a Python function that checks whether a passed in string is palindrome or not.
def palindrome(s):
    s=s.lower()
    index=-1
    for letter in range(0,int(len(s)/2)):
        if s[letter] != s[index]:
            print("not palindrome")
            return False
        else:
            index -=1
    print("is palindrome")
    return True
palindrome("helleh")
#"nurses run" - for this case: I think to create a list
def palindromeF(s):
    sList=s.lower().split() #this creates a list with the words, not letters, this ex. => [nurses, run]
    concatWord="".join(sList)
    #concatenate
    print(concatWord)
    index=-1
    for letter in range(0,int(len(concatWord)/2)):
        if concatWord[letter] != concatWord[index]:
            print("not palindrome")
            return False
        else:
            index -=1
    print("is palindrome")
    return True
palindromeF("Nurses Run")