# lis = ["ab","walter white","hello","holla"]

# newst = "Hello Walter white"

# newst = newst.replace('e',"o")

# print(newst)

# mylist = [-1,2,5,66,78,2,3,-8,-9,0,-5]
# lis.sort()
# print(lis)
# mylist.sort()
# print(mylist)

# cars = ['Ford', 'BMW', 'Volvo']

# cars.sort()

# print(cars)

# print("sorted function : ",sorted(cars))

# newlist = [0] * 5

# newlist1 = [12,5,6,7,7]
# print(type(newlist))
# print(type(newlist1))

# n =  newlist + newlist1 

# print(n)

# for i in range(5):
#     # print(i)
#     for j in range(5):
#         print("*",end=" ") #by default end = "\n" ,here printing sace after each star printed.
#     print()#then adding new line after each iteration.

# import numpy as np

# val=np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]])
# print(val.ndim)
# print(val)

# val1= np.ones((5,5))

# val1[1:4,1:4] = 0
# val1[2,2]=9
# print(val1)

# print(val[:,1])

# mytuple = [3,5,7]

# a,*b = mytuple

# print(a)



# mydict = dict(a=1,b=2)

# print(mydict["a"])
# print(mydict.items())
# for key in mydict:
#     print(key)


# t1t = (1, 5, 6)
 
# t2t = (1, 5, 6)
 
# # show the id of object
# print("t1t",id(t1t))
 
# print("t2t",id(t2t))


# t1l = (1, 5, 6)
 
# t2l = (1, 5, 6)
 
# # show the id of object
# print("t1l",id(t1l))
 
# print("t2l",id(t2l))


# mytuple = ('abc')#this will consider as a str

# print(type(mytuple))


# mytuple = ('abc',)#this will consider as a tuple

# print(type(mytuple))


#Sets  : unordered , mutable , no duplicates

# mysetnew = {}
# print(type(mysetnew))#this will consider as a dict not as a set

# myset = set()

# myset.add(1)
# myset.add(2)
# myset.add(3)

# myset.remove(3)

# or 

# myset.discard(3)

# print(myset)

# odds ={1,3,5,7}

# evens = {0,2,4,6}

# prime = {2,3,5,7}

# newsets = odds.union(evens)

# intersec = odds.intersection(prime)

# print(newsets)

# print(intersec)

# setA = {1,2,3,4,5,6,7,8,9}
# setB = {1,2,3,10,11,12,}

# diffodd = setA.difference(setB)

# diffeve = setB.difference(setA)

# print(diffodd)
# print(diffeve)

# sydiff = setA.symmetric_difference(setB) #print only the uncommon elements

# print(sydiff)

# setA.update(setB)
# setA.intersection_update(setB)#only print common elements from both sets

# setA.difference_update(setB)#only print the elements uncommon in setA 
# setC = {3,4}
# setD ={18}
# print(setC.issubset(setA))

# print(setA.issuperset(setC))

# print(setA.isdisjoint(setD))

# set_new = {1,2,3,4}

# set_new1 = set_new

# set_new1.add(5)

# print(set_new1)#here the original set also added the new element 
# print(set_new)


# set_new = {1,2,3,4}

# set_new1 = set(set_new)

# set_new1.add(5)

# print(set_new1)#here the original set not added the new element 
# print(set_new)

# a = frozenset([1,2,3,4])

# a.add(5)
# print(a)


# Strings: ordered, immutable , text representation 


# my_string = "I'm a programmer"
# print(my_string)

# my_string = """Hi 
# programmer"""
# print(my_string)

# my_string = """Hi  \
# programmer"""
# print(my_string)

# my_string = "Hello World"

# char = my_string[::-1]

# print(char)

# a = "Hello"

# b = "Athisruth"

# sentence = a + " " + b

# print(sentence)

# mystring = ' Hello World '
# print(mystring)
# mystring = mystring.strip()#used to remove the space in the starting and end strings.
# print(mystring)
# ne = mystring.split()
# print(ne)


# mystring = 'Hello World'
# print(mystring.startswith("H"))
# print(mystring.endswith("d"))
# print(mystring.find("l"))#print the first index position.If it does not fing any string or substring(eg:'ab') it show -1.
# print(mystring.replace("World","Athisruth"))
# print(mystring.replace("World","Athisruth"))
# mystring = 'Hello,World,hi,all'
# ne = mystring.split(",")
# newstring=" ".join(ne)
# print(ne)
# print(newstring)


# from timeit import default_timer as timer
# mylist = ['a'] * 1000000
# # print(mylist)

# #bad
# start = timer()
# my_string = ""
# for i in mylist:
#     my_string += i #here we cancatenating ne elements to an empty string.
# stop = timer()
# print(stop-start)
# # print(my_string)

# #good
# start = timer()
# my_string ="".join(mylist)
# stop = timer()
# print(stop-start)
# print(my_string)


# format methods

# var = "Tom"

# mystring = "the variable is %s" % var

# print(mystring)

# var = 5

# mystring = "the variable is %d" % var

# print(mystring)

# var = 5.43673883

# mystring = "the variable is %f" % var

# print(mystring)

# var = 5.43673883

# st = "hi"

# mystring = "the variable is %.2f %s" %(var,st) #.2f to mention the number of decimal points.

# print(mystring)


# var = 5.43673883

# st = "hii"

# mystring = "the variable is {:.2f} {}".format(var,st)#:.2f to mention the number of decimal points.

# print(mystring)


# var = 5.43673883

# st = "hii"

# mystring = f"the variable is {var} {st}"

# print(mystring)


# Collection: Counter , namedtuple , OrderedDict , defaultdict ,deque

# Collections in Python are containers used for storing data and are commonly known as data structures, such as lists,tuples, arrays ,sets,dictionaries,etc.
# Python has a build-in collections module providing additional data structures for collections of data.

# from collections import Counter 

# a = "aaaaabbbbccc"
# my_counter = Counter(a) #using counter module we can make string values as key values(dictionaries) based on the element and its count.
# print(my_counter)
# print(my_counter.most_common(1))#print most counted element.
# print(my_counter.most_common(1)[0][0])
# print(list(my_counter.elements()))

# print(list(a))


# from collections import namedtuple

# Point = namedtuple('Point','x,y')#used to name a tuple
# pt = Point(1,-4)
# print(pt)
# print(pt.x,pt.y)#to print the values for x and y.

# from collections import OrderedDict

# oredred_dict = OrderedDict() 
# oredred_dict["b"] = 2
# oredred_dict["c"] = 3
# oredred_dict["d"] = 4
# oredred_dict["a"] = 1
# print(oredred_dict)


# from collections import defaultdict

# d = defaultdict(int)#we can set default datatype 
# d['a'] = 1
# d['b'] = 2
# print(d['b'])
# print(d['c'])#print new key values as '0'.

# b = defaultdict(float)#we can set default datatype 
# b['a'] = 1
# b['b'] = 2
# print(b['b'])
# print(b['c'])


# b = defaultdict(list)#we can set default datatype -type of the element.
# b['a'] = 1
# b['b'] = 2
# print(b['b'])
# print(b['c'])


# b = {} #here we can get errors if we fetch an unknown key.
# b['a'] = 1
# b['b'] = 2
# print(b['c'])


# from collections import deque

# d = deque()#used to append elements.

# d.append(1)
# d.append(2)
# d.appendleft(3)
# print(d)
# # d.popleft()
# # d.clear()
# # d.extend([4,5,6])
# d.extendleft([4,5,6])
# print(d)
# d.rotate(1)
# d.rotate(-1)
# print(d)

# Itertools: product , permutations,combinations,accumulate,groupby, and infinite iterators
# -itertools module is a collection of tools to handle different types of iterators.

#Iterators are the data types that can be used in a for loop. 

# a = "ashshs "
# for i in a :
#     print(i)


# from itertools import product

# a = [1,2]
# b = [3]
# prod = product(a,b,repeat =2)#to get the product.
# print(list(prod))

# from itertools import permutations

# a = [1,2,3]
# perm = permutations(a)
# print(list(perm))


# from itertools import combinations,combinations_with_replacement,count,cycle,repeat

# a = [1,2,3,4]
# comb = combinations(a,2)
# print(list(comb))

# a = [1,2,3,4]
# comb_wr = combinations_with_replacement(a,2)
# print(list(comb_wr))


# from itertools import accumulate
# import operator 
# a = [1,2,5,3,4]
# acc = accumulate(a , func =operator.mul)
# acc = accumulate(a , func = max)
# print(list(acc))
# n = []
# for i in range(1,len(a)+1):
#     star = sum(a[:i]) 
#     n.append(star)
# print(n)
# print(sum(a[:1])+a[2])


# from itertools import groupby
# def smaller_than_3(x):
#     return x<3
# a = [1,2,3,4]
# group_obj =groupby(a,key=smaller_than_3)

# for key,value in group_obj:
#     print(key, list(value))


# from itertools import groupby
# a = [1,2,3,4]
# group_obj =groupby(a,key=lambda x: x< 3 )

# for key,value in group_obj:
#     print(key, list(value))


# from itertools import groupby

# persons = [{'name':'Tim','age':25},
#            {'name':'Dan','age':25},
#            {'name':'Lisa','age':27},
#            {'name':'Claire','age':28}]
# a = [1,2,3,4]
# group_obj =groupby(persons,lambda x: x["age"])

# for key,value in group_obj:
#     print(key, list(value))


# from itertools import count,cycle,repeat

# for i in count(10):#print number infinitly from 10.
#     print(i)
#     if i == 1000:
#         break



# from itertools import count,cycle,repeat
# a=[1,2,3]
# for i in cycle(a):#print the same number as a cycle from 1,2,3..1,2,3...
#     print(i)


# from itertools import count,cycle,repeat
# for i in repeat(1)#here number 1 repeat infinite times.
#     print(i)
# for i in repeat(1,4)#here number 1 repeat 4 times.
#     print(i)
   

# lambda arguments:expression


   









































