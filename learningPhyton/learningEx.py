from operator import index
import math

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
