#assert<condition>
#assert<condition><error messsage>



#In Python, the assert statement is used to continue the execute if the given condition evaluates to True.
#If the assert condition evaluates to False, then it raises the AssertionError exception with the specified error message.



# x = "hello"

# #if condition returns True, then nothing happens:
# assert x == "hello"
# print('x==hello,statement True')


# #if condition returns False, AssertionError is raised:

# assert x == "goodbye",'x != goodbye'



# assert True
# print('Hii')

# assert False,'condition is false'
# print('Hii')
# print('Heloo')

# assert 'jango' in 'Django is a python web development application','jango not in the string'
# print('jnagio is a python application')

# assert 'Django' in 'Django is a python web development application'
# print('Djnagio is a python application')

# str1='python'
# str2='python'
# assert str1==str2
# print('python is very easy to learn')


# assert 'python' in ['Python','cpp','java'],'python not in the list'
# print('python')

# from math import*
# assert sqrt(4)==2,'condition is false'
# print('passed')

# import math
# assert math.sqrt(4)==2,'condition is false'
# print('passed')

# def age(a):
#     assert a>0,'not a valid number'
#     print('my age is:',a)
# a=int(input('enter the age: '))
# age(a)
#############################

# def avg(marks):
#     assert len(marks)!=0,'list is empty'
#     print('passed')
#     return sum(mark1)/len(marks)
# mark1=[1,2,3,4,7,9,9,65]
# print(avg(mark1))

# from statistics import mean
# def avg(marks):
#     assert len(marks)!=0,'list is empty'
#     print('passed')
#     return mean(mark1)
# mark1=[1,2,3,4,55,7,8,5]
# print(avg(mark1))



