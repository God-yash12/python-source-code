
#Lets start learning python from scratch  we do comment using '#'
# main one thing to notice is indentation which is spacing 

# 1. Syntax and Basic Data Types

# a = "ram" #string
# b = 3 # integer
# c = 3.23 # float
# d = True #boolen

# <------------multiline string-------------------->
# a = """this is me ganesh thapa 
# from gulmi and lives in butwal with purpose of making good life """
# print(a[1])

# print(a, b, c, d)  # printing statement

# for x in "banana":     #loops through string
#   print(len(x))

# <----------- In python we can check the value of string using in and if the value is not preesent in the string then we can use not in statements   for example --------------------------->

# text = "This is motherFucker is here"
# if "there" in text:
#     print("here is present")
# elif "there" not in text:
#     print("here is not present")

#<------- there is a way to modify the string in uppercase, lowercase,  remove whitespace, replace, split---------------->

# a= "  this, is me"
# print(a.capitalize())
# print(a.upper())
# print(a.lower())
# print(a.split(","))
# print(a.replace("this", "hehe"))
# print(a.strip())
    
# message = "I love you "
# times = 3000
# concatenation = message + "" + str(times) + "!"

# print(concatenation)

#<---------- Formatting String in python and it is representated by "f" and placeholder in python ---------------->

# a= 34
# text = f"Mango is expensive and its price is {a} dollers" # the f representated the formatted string and let to palce a placeholders
# print(text)

# Text = f"multiplication of {33 * 44} is answer"
# floatPlace = f"this is float palceholder {33.33 * 334:.2f}" # the 2f represent the vlaue after decimal numbers in this the float value is 2 after decimal.
# print(Text)
# print(floatPlace)



#<--------- Escape Character in Python is represent by /sbfsbfisbfjs/ backshalsh ------------------------------>
# txt = "We are the so-called \"Vikings\" from the north."
# print(txt)

# note: other excape character are //, /n for new line, /r for Carriage return, /t tab, /b backslash, /f from feed, /ooo octal value and /xhh hex value --------------------------------------------------->


#<-------- check the string methods such as split, index, rstrip, split, uppercase(), lower more more as we needed ------------------------------>


#<------ Boolean in Python returns True and False when the condition is match ------------------->
# only the condition is false when the value, list, sets, Dictionary, Tuples are empty and number is "0" ------------------------->


#<----------- Operation in Python are like in Javascript  such are   Arithmetic operators
# Assignment operators
# Comparison operators
# Logical operators
# Identity operators
# Membership operators
# Bitwise operators --------------------------------------------------->


# 2. Control Structure such as If elif and else // for while loop

# IF statement 

# x = 26
# if x > 18:
#     print("he is teenager")
# elif x == 22:
#     print("He is young")
# else:
#     print("He is going to be a man")


# For While loop

# for i in range(5):
#     print(i)    
    
    # While loop
    # count = 5
    # while count < 5:
    #     print(count)
    #     count += 1
        
        
# 3. Functions 

# def fuck(you):
#     return "Fuck you" + " " + you

#  function calling
# message = fuck("Madarchod")
# print(message)
        
        # if i use "Global" keyword inside the function then the variable can be accessible from the global palce or globally.         
        
# 4. Data Structure

#<------------------------ Lists -------------------------------------->

# myLists = ["Ganesh", "Ram", 333, 4544]
# herList = [1, 3, 5, "OLALALA"]
# print(myLists)
# print(myLists[2])  # Accessing element from list

# myLists.append("Site")  # Add value
# print(myLists)

# myLists.pop() # remove last element and retrun the list
# print(myLists)

# myLists.extend(herList) # add to element or lists 
# print(myLists)

# myLists.insert(2, "Timi nai hau Malai maya garne ney timi nai hau timi nai hau")
# print(myLists) # insert to helps to add element in the position wherever you want the indexing is start from 0 i have added at 2 index 

# myLists.remove("OLALALA")
# myLists.remove(333)
# print(myLists)  # remove the element from lists 

# myLists.index("Ganesh")
# print(myLists)

# the is also negative indexing in python where it count the data from backwards 
# print(myLists[-1])

# we can print the lists item from one range to another such as using :, 
# print(myLists[1:3]) # however also explore :3, 2: ect like that 
# print(myLists[:2])
# print(myLists[2:])

# print(myLists[-3: -1])
# we can also check the item is in list or not by using "in" or "not in" 

#<----------- Changing the list values ------------------>
# myLists[1] = "Habibibbbb"
# print(myLists)

#<--------- changing the range of value using :----------------------

# myLists[1:3] = ["Olalal", "Golala", "Messi"]
# print(myLists)
#<----- Inserting new value using insert value -------------->
# myLists.insert(2, "bububububububububu")
# print(myLists)

#<----- Remove and del keywords also use to remove item from list del also delete the list form code. and pop(2) also remove index item of list --------------->

#<------ Loop in Lists ------->

# for a in myLists:
#     print(a)

# for a in range(len(myLists)):
#     print(myLists[a])

# thislist = ["apple", "banana", "cherry"]
# i = 0
# while i < len(thislist):
#   print(thislist[i])
#   i = i + 1


#<------- List Comprehension ----------------->

# myLists = ["Ganesh", "Ram", 333, 4544]
# newList = []

# for x in myLists:
#     if isinstance(x, str) and "a" in x:   # becasue of mylist doesnot contain all strings so i use instance and str to change the int value into string
#         newList.append(x)
# print(newList)
   # this print the name or string only containting a letter  in the words 

#<------- creating copy of list using copy() -------------->

# myLists = ["Ganesh", "Ram", 333, 4544]
# thisList = myLists.copy()
# print(thisList)

#using list property 
# thisLists = list(myLists)
# print(thisLists)

#<-------------- Don't forget to revise the list methods all sort, reverse, expand, extend, remove(), pop(), index(), count(), copy(), clear(), insert() alll------------------------>

# for i, item in enumerate(myLists, start=1):  # this enumerate helps to print the list with order lists
#     print(i, item)


# The difference between Lists and Tuples are Lists are represented by [] and tuples are () lists are mutable or changeable where tuples are unmutable and unchangeable



# Lets Learn about Tuples and Its use cases 
# 1. Tuples are immutable, unchangeable and can be anytype such as string, number and other tuple  it is commonly used to store Cartesian Coordinate  that is (X, Y) example  points = 10, 20, database recording 

# <----------------Creating Tuples  _------------------>
# if we are writting tuple of one word the we write in using comma 
# tupleis = ("ram",)
# print(type(tupleis))


#<-------------- using tuple constructor -------------------->
# myTuples = tuple(("ganesh", "Ram", " Hari", 2, 234,45, 56, 23))  # use 2 (()) to create tuple constructor
# print(type(myTuples))


#<------ Tuples are unchangeable but we can change its value by converting it into list -------------- example =/>

# myTuples = tuple(("ganesh", "Ram", " Hari", 2, 234,45, 56, 23))  
# xxx = list(myTuples)   # converting tuple into list 
# print(xxx)                       
# xxx.insert(1, "bebebebe")
# print(xxx)
# zzz = tuple((xxx))
# print(type(zzz))  # conveting list into tuple again

# myTuples = ("Ram", "ganesh", 1, 34, 67)
# myTuples = tuple("ram", 1, 2, 3) # we can create tuple using tuple constructor
# print(myTuples)

# points = (20, 40)
# x, y = points   # unpacking
# print(points)

# unpacked = (2, "hehehe", 34, 45, "hbdfus" "hahaha")
# ( Ram, Ganesh, *mine) = unpacked 
# print(Ram)
# print(Ganesh)
# print(mine)

#<---- the is only 2 methods  of tuple such as count() and index()------------------->


#<---- Unpacking---------> The unpacking tuples means that splitting tuple elements into individual elements in above element 20 and 40 are splitted into x and y 

# <---------- Unpacking with (* ) ------------>
# steps = (1, 2, 34,5, 6,7,8,5)
# x, *rest, y = steps
# print(x)
# print(y)
# print(rest)



#<---------- Function Argument and Tuples ------------>

# def myTuples():
#     return "Ganesh", 23, "Gulmi"

# name, age, address = myTuples()
# print(name)
# print(age)
# print(address)


#<--------- Dictionary in python -------------->
#<--- dictionary in python is like kinda of object in javascript the it store the data within key-value pairs suchas name: Ganesh,  it is use to store key value pairs it is changeable, ordered and non-duplicates 

# my_dict = {
#     "Name": ["Ganesh", "Ram", "Sita", "Hari"],
#     "Address":["Gulmi", "Butwal", "Janakinagar", "Isma"],
#     "Age": [12, 34, 44, 11]
# }
# print(my_dict)
# print(my_dict.get("Address"))
# print(my_dict.keys())
# my_dict["car"] = "Bugati cheron 49000"
# print(my_dict)
# print(my_dict.values())

# print(my_dict.items())

#<---- changing values in dictionaries --------->

# my_dict.update({"age": 23})   # this is for single key value pair to update the dictionary:

# my_person = my_dict["Name"].index("Ganesh")
# my_dict["Age"][my_person] = 90
# print(my_dict)


#<---- removing item from dictinoary using pop and popitem and del and clear

# del my_dict["Age"]
# my_dict.clear() empty the dictiunary
# for x, y in my_dict.items():
#     print(x, y)

#use dict() method to copy the dictionary 

# <-------------------- Nested Dictionary --------------------------->

# bebe1 = {
#     "name": "heerree", 
#     "Age": 22
# }

# bebe2 = {
#     "name" : "saru",
#     "Age" : 23
# }

# bebe3 = {
#     "name" : "sita",
#     "Age" : 21
# }


# myDictionary = {
#     "bebe1" : bebe1,
#     "bebe2" : bebe2,
#     "bebe3" : bebe3
# }

# # print(myDictionary)
# print(myDictionary["bebe1"]["name"])
# print(myDictionary["bebe1"].values())

#<------ Methods in Dictionary --------------> clear, copy, fromkeys, get, items, keys, pop, popitem, setdefault, updates and values.




#<--------- Lambda Function in Python -------------> a lambda is a small function which takes any number as argument and have only one expression 
    # <- -- lambda = argument : expression

# x = lambda a : a* 10
# print(x(89))

# using lambda inside  a function 

# def myFunction(m):
#     return lambda a : a * m 
# mylambo = myFunction(3)

# print(mylambo(20))


#<----------- Arrays in Python -------------------->
# lists can be use as array in python there is no built in function or array in python however we can import libraries numpy pandas to use array.------------->

#< ---------- math in Python ---------->

# x = min(5, 10, 25)
# y = max(5, 10, 25)

# print(x)
# print(y)

# xx = abs(-389457.23) # abs provides the absolute positive number of negative  number
# print(xx)

# xxx = pow(3, 5)  #pow provides the power of the item, where 3 is base and 5 in exponent or exponential
# print(xxx)

# xxa = 3 ** 5
# print(xxa) #same thing
# import math

# # the sqrt provides the square root of the number 
# n = math.sqrt(59)
# nn = math.ceil(3434.33334678)
# nnn = math.floor(343.3423211)
# xn = math.pi
# print(xn)
# print(nnn)

# x = str("Ganesh Thapa") # the str in this code called casting of data type
# x = (type(1))  # the type print the type of data type such as string number or string etc














# <------------- Python "SET" Data collection (arrays) -------------------> 
# set is unchangeable, unindexing, and unordered data sets where we can store a lot values in one variable it is written inside {} ----------->  but we can add remove sets elements---------------->

# mySet = {"Gensh", "Hari", "hehehe", "hahaha", 2, 3, 4, 5,4,3}
# addSets = {"sdh", "hehue", "hahaha"}
# mySet.update(addSets)
# print(type(mySet))
# mySet.add("hello motherfucker")
# print(mySet)
# use doscard method to remove item from set. also we can use remove, pop, clear to remove item form the set

# x = list(mySet)
# print(type(x))

#<---- Set can be add, remove, add, access, join, and methods --------->

#<-------- join---------------->
# set1 = {"this", "is", "me", "hellp"}
# set2 = {1, 3,4 ,5,6, 4}

# set1 = set1.union(set2)
# print(set1)
# print(set1 | set2)    # "|" called union ()
 
# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = {"John", "Elena"}
# set4 = {"apple", "bananas", "cherry"}

# myset = set1 | set2 | set3 |set4
# print(myset)

# set6 =  set3.difference(set4) 
# print(set6)

#<------------- Set Methods ----------------------->  add, clear, copy, difference, difference_update, discard, intersection, intersection_update, isdisjoint, isdisjoint_udpate, pop, issubset, issuperset, remove, symmetric_difference, symmetric_difference_update, union, update. ------------>

