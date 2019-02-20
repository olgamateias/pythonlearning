from tarfile import pwd
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
"""
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
mode='r' is read only
mode='w' is write (will overwrite files or create new ones
mode='a' is append only (will add on to files)
mode='r+' is reading and writing
mode='w+' is writing and reading (overwrites the existing files or creates a new one!)
"""
 




