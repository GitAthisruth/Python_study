# print('first value is {a} and second value is {b}'.format(a="tom",b=53663))
# # n=(1,2,3,4)
# print('the first value is %s and second value is %d and third value is %f'% ('tom',.53663,.647846) )
# a=10
# b=8
# if a>b:
#     print("a is greater than",b)
#     c=10
#     if a>100:
#         pass
#     else:
#         print('a is not greater',100)
#         if a==c:
#             print(a,"is equal to",c)
# else:
#     print('sorry')    
# print('first value is %(a)s and %(2)d'%{'a':'Tom','2':56565})
# t=53646
# r='Tuco'
# print(id(r),id(t))
############################
# a=26
# b=input('type a number: ')
# if b>a:
#     print(b,'greater than',a)
# elif b<a:
#    print(b,'less than',a)
# elif b==a:
#    print(a,'equals to',b)
# else:
#     print('incorrect input')      
# a={1:'Tuco',2:'Saul Goodman',3:'Salamanga Brothers'} 
# #replace value
# # a[3]='sumesh' 
# # print(a) 
# # append value 
# a['Hank']='Gustavo Fring'
# print(a)
# a=[]
# for i in range(3):
#     b=int(input('Enter the values: '))
#     a.append(b)
# print(a)
# sum=0
# for r in a:
#     sum=sum+r
# print(sum)

# a=6.9
# a=int(a)
# print(a)

# def avg(val):
  
#     for i in range(val):
#         sum=0

        
#         avrg=int(input('enter the values: '))
#         sum=sum+avrg
#         a=sum/val
#     print(a)
# avg(int(input('enter the count: '))) 
###########################

# def valve():
#     a=dict(e='Walter',b='Jesse',c='Mike',d='Gustavo')
#     print(a)
#     for i,j in a.items():
#         pass
#     return i,j
# g=valve()
# def sum():
#     r=0
#     t=[1,2,3,4,5]
#     for k in t:
#         r=r+k         
#     return r
# q=sum()
# k=[g,q]
# print(k)
#########################

# def ls(n):
#         if len(n)==1:
#             return n[0]
#         else:
#             return n[0] + ls(n[1:])
# print(ls([1,2,3,4,5]))

# def ls(n):
#     total=0
#     for i in n:
#         if type(i)==type([]):
#             total=total+ls(i)
#         else:
#             total=total+i
#     return total
# print(ls([1,2,[3,4],[5,6]]))


# def add(c):
#     return c*5
# def mult(c):
#     return c*5
# print(mult(add(5)))

# import sys
# sys.setrecursionlimit(80000000)
# print(sys.getrecursionlimit() )  

# def sum():
#     print('Hello')
#     sum()
# sum()  
# 
###################### 
#calculator
######################
# a=float(input('Enter the first number: '))
# op=input('Enter the operator: ')
# b=float(input('Enter the second number: '))
# if op=='+':
#     print(a+b)
# elif op=='-':
#    print(a-b)
# elif op=='*':
#     print(a*b)
# elif op=='/':
#     print(a/b)
# elif op=='%':
#     print(a%b)
# elif op=='&':
#     print(a&b)
# elif op=='|':
#     print(a|b)
# elif op=='^':
#     print(a^b)
# else:
#     print('invalid input')
    



# def cal(a,op,b):

#     if op=='+':
#        return(a+b)
#     elif op=='-':
#         return(a-b)
#     elif op=='*':
#         return(a*b)
#     elif op=='/':
#         return(a/b)
#     elif op=='%':
#         return(a%b)
#     elif op=='&':
#         return(a&b)
#     elif op=='|':
#         return(a|b)
#     elif op=='^':
#         return(a^b)
#     else:
#         print('invalid input')


# a=float(input('Enter the first number: '))
# op=input('Enter the operator: ')
# b=float(input('Enter the second number: '))
# t=cal(a,op,b)
# print(t)


# a=dict([(1,'r'),(2,'o')])
# a.update(l='u',y='p')
# print(a)

# lim=int(input('enter the limit: '))
# a=[]
# for i in range(lim):
#     e=input('enter values: ')
#     a.append(e)
# print(a)
######################



# def call(g):
#     a=[]
#     for i in g:
#         g=float(input('Enter the value: '))
#         a.append(g)
#     return a
# g=int(input('Enter the count'))
# print(call(g))


# a=float(input('Enter a value: '))
# b=float(input('Enter a value: '))
# c=float(input('Enter a value: '))
# d=a+b+c
# print('The area of {} triangle is {}'.format(a+b+c,d))
# print('the area of a triangle is %f,%d'%(d,d))



########################################################################################################################

# print(r'\ttelevision')

# print('\ntelevision')



# import re

# text_to_search = '''
# abcdefghijklmnopqrstuvwxyz
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
# 1234567890
# Ha HaHa .077
# MetaCharacters (need to be escaped):
# . ^ $ * + ? { } [ ] \ / ( )
# coreyms.com
# 321-555-4321
# 123.555.1234
# 123*555*1234
# 900-555-1234
# Mr. Schafer
# Mr Smith
# ms Davis
# Mrs. Robinson
# Mr. T
# '''



# pattern=re.compile(r'\.')
# matches=pattern.finditer(text_to_search)
# for match in matches:
#     print(match)
  


# pattern=re.compile(r'.')
# matches=pattern.finditer(text_to_search)
# for match in matches:
#     print(match)
  


# patternce=re.compile(r"\s")#it will match spaces newline(\n) and tab(\t)
# matches=patternce.finditer(text_to_search)
# for match in matches:
#     print(match)



# patternce=re.compile(r"\bHa")#it will match without spaces newline(\n) and tab(\t)
# matches=patternce.finditer(text_to_search)
# for match in matches:
#     print(match)




# patternce=re.compile(r"\BHa")#it will match spaces newline(\n) and tab(\t)
# matches=patternce.finditer(text_to_search)
# for match in matches:
#     print(match)


# sentence='Start a sentence and then bring it to an end'

# patternce=re.compile(r"nd$")
# matches=patternce.finditer(sentence)
# for match in matches:
#     print(match)



# text_to_search = '''
# abcdefghijklmnopqrstuvwxyz
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
# 1234567890
# Ha HaHa .077
# MetaCharacters (need to be escaped):
# . ^ $ * + ? { } [ ] \ / ( )
# coreyms.com
# 321-555-4321
# 123.555.1234
# 123*555*1234
# 900-555-1234
# Mr. Schafer
# Mr Smith
# ms Davis
# Mrs. Robinson
# Mr. T
# '''


# import re

# pattern=re.compile(r'\d{3}\W\d{3}\W\d{4}')
# with open('C:/Users/athis/Downloads/data.txt') as file:
#      content=file.read()
#      matches=pattern.finditer(content)
# for match in matches:
#     print(match)


# import re

# pattern=re.compile(r'\d{3}.\d{3}.\d{4}')
# with open('C:/Users/athis/Downloads/data.txt') as file:
#      content=file.read()
#      matches=pattern.finditer(content)
# for match in matches:
#     print(match)

# import re

# pattern=re.compile(r'\d{3}\S\d{3}\S\d{4}')
# with open('C:/Users/athis/Downloads/data.txt') as file:
#      content=file.read()
#      matches=pattern.finditer(content)
# for match in matches:
#     print(match)


# import re

# text_to_search = '''
# abcdefghijklmnopqrstuvwxyz
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
# 1234567890
# Ha HaHa .077
# MetaCharacters (need to be escaped):
# . ^ $ * + ? { } [ ] \ / ( )
# coreyms.com
# 321-555--4321
# 123.555.1234
# 123*555*1234
# 800*-555-1234
# 800--555-1234
# 900--555-1234
# Mr. Schafer
# Mr Smith
# ms Davis
# Mrs. Robinson
# Mr. T
# '''


# pattern=re.compile(r'[89]00[*--].\d{3}[-]\d{4}')#here [*--] check a digits with  * then - and last again -(we should give it orderly otherwise it fetch error ) 
# matches=pattern.finditer(text_to_search)
# for match in matches:
#     print(match)



# import re

# text_to_search = '''
# abcdefghijklmnopqrstuvwxyz
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
# 1234567890
# Ha HaHa .077
# MetaCharacters (need to be escaped):
# . ^ $ * + ? { } [ ] \ / ( )
# coreyms.com
# 321-555--4321
# 123.555.1234
# 123*555*1234
# 800*-555-1234
# 800--555-1234
# 900--555-1234
# Mr. Schafer
# Mr Smith
# ms Davis
# Mrs. Robinson
# Mr. T
# cat
# pat
# mat
# bat
# '''


# pattern=re.compile(r'[cpm]at')
# matches=pattern.finditer(text_to_search)
# for match in matches:
#     print(match)

# pattern=re.compile(r'[^b]at')
# matches=pattern.finditer(text_to_search)
# for match in matches:
#     print(match)



# import re

# text_to_search = '''
# abcdefghijklmnopqrstuvwxyz
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
# 1234567890
# Ha HaHa .077
# MetaCharacters (need to be escaped):
# . ^ $ * + ? { } [ ] \ / ( )
# coreyms.com
# 321-555--4321
# 123.555.1234
# 123*555*1234
# 800*-555-1234
# 800--555-1234
# 900--555-1234
# Mr. Schafer
# Mr Smith
# ms Davis
# Mrs. Robinson
# Mr. T
# cat
# pat
# mat
# bat
# '''


# pattern=re.compile(r'(Mr|ms|Mrs).?\s[A-Z]\w*')
# matches=pattern.finditer(text_to_search)
# for match in matches:
#     print(match)



# pattern=re.compile(r'(Mr|ms|Mrs).?\s\w*')
# matches=pattern.finditer(text_to_search)
# for match in matches:
#     print(match)




# import re

# emails ='''
# miketyson@gmail.com 
# miketyghhffson@gmail.com 
# henry.cavill@university.edu
# jason-321-statham@my-work.net
# '''

# pattern=re.compile(r'[\w+-.]+@[\w+-]+\.(com|edu|net')#'[\w+-.]+' in this '+'(1 or more) means it takes multiple characters.
# matches=pattern.finditer(emails)
# for match in matches:
#     print(match)

 
# pattern=re.compile(r'[\w+-.]+@[\w+-.]+(com|edu|net)')
# matches=pattern.finditer(emails)
# for match in matches:
#     print(match)



# urls ='''
# https://www.google.com
# http://isro.com
# https://youtube.com
# https://www.nasa.gov
# '''

# import re

# pattern=re.compile(r'https?.{3}[\w+.]+(com|gov)')
# matches=pattern.finditer(urls)
# for match in matches:
#     print(match)


#arrays

# from numpy import*

# a=array(1)

# print(a)

# b=array([1,2])

# print(b)

# c=array([[1,2],[1,2]])

# print(c)

# d=array([[[1,2],[1,2]],[[1,2],[1,2]]])

# print(d.ndim)

# d=array([[[[1,2],[1,2]],[[1,2],[1,2]]]])


# print(d.ndim)

# d=array([[[[[1,2],[1,2]],[[1,2],[1,2]]]]],dtype='str')


# print(d.ndim)

# print(type(d))


# val=array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]])
# print(val)

# print(val.shape)
# # print(val[1])
# print(val[0])

# print(val[0][3])

# print(val[1:2]) #here 1 is the first element,2 is range(0,1),here take 1 to 1.
 
# print(val[0:2]) 

# print(val[2:]) 

# print(val[1:3]) 

# print(val[0,:]) 

# print(val[0,2:5])

# print(val[0,:])  

# print(val[0,3]) 

# print(val[0,3])  



# val=array([[1,2,3,4,5,6,7,8],[9,10,11,12,13,14,15,16]])

# print(val)


# print(val[0,1:6:2])  


# val[0,4] =  56

# print(val)

# val[:,2]=34,89
# print(val)

#  
# val[0,2],val[1,2]  =45,67

# print(val)




# val=array([[[1,2,3,4,5],[6,7,8,9,10]],[[11,12,13,14,15],[16,17,18,19,20]]])


# print(val[:,:,0])

# import numpy as np

# val=np.array([[[1,2,3,4,5],[6,7,8,9,10]],[[11,12,13,14,15],[16,17,18,19,20]]])

# print(val.ndim)
# print(val)


# [[1. 1. 1. 1. 1.]
#  [1. 0. 0. 0. 1.]
#  [1. 0. 9. 0. 1.]
#  [1. 0. 0. 0. 1.]
#  [1. 1. 1. 1. 1.]]




# import numpy as np

# val=np.ones((5,5))
# print(val)

# val[1:4,1:4]=0

# print(val)

# val[2,2]=9

# print(val)


# import numpy as np


#Mathematical operations


# a=np.array([[1,2,3,4],[5,6,7,8]])

# # print(a)

# b=np.array([[1,2,3,4],[5,6,7,8]])

# print(a+b)

# print(a+b)
# print(a+5)

# print(np.cos(a))


# a=np.ones((2,3))

# print(a)
# print()

# b=np.full((3,2),3)

# print(b)

# print()

# print(np.matmul(a,b))


# val=np.array([[1,2,3],[1,1,1]])

# print(val)
# print()

# val1=np.array([[1,2],[1,1],[1,1]])
# print(val)
# print()


# print(np.matmul(val,val1))

# arr=np.identity(3)

# print(arr)

# print(np.linalg.det(arr))


# val=np.array([[1,2,3,4],[5,6,7,8]])
# print(val)

# print(np.min(val))
# print(np.max(val))
# print(np.mean(val))
# print(np.median(val))


# val=np.array([[1,2,3,4],[5,6,7,8]])
# print(val)

# print(val.shape)

# val1=val.reshape(4,2)
# print(val1)

# val2=val.reshape(1,4,2)
# print(val2)

# print(val.itemsize)


# a=np.array([[1,2,3,4]])

# print(a)
# print()

# b=np.array([[5,6,7,8]])

# print(np.vstack([[[a,b]]]))

# c=np.hstack([[[a,b,a,b,a]]])
# print(np.arange(1,5,1))

# print(np.linspace(1,5,15).reshape(3,5,1))


# import matplotlib.pyplot as plt

# import numpy as np

# x= np.array([1,2,3,4])
# y=x**2

# plt.title('Square')

# plt.xlabel('x-axis')

# plt.ylabel('y-axis')
# plt.plot(x,y,'purple')
# plt.savefig('figure2.png')
# plt.show()

# size=[5,6,8,9,23,30]
# labels=['a','b','c','d','e','f']
# colors=['purple','red','green','yellow','blue','c']
# explode=[0,0.1,0,0.2,0,0.3]
# plt.title('PIE_CHART')

# plt.pie(size,explode=explode,colors=colors,labels=labels)

# plt.savefig('Fig_pie.png')

# plt.show()



#Series

# import pandas as pd

# data=[1,2,3,4]

# a=pd.Series(data,index=['a','b','c','d'],dtype=float,copy=True)

# print(a)



# import pandas as pd

# import numpy as np


# data={'a':[1,2,3,4,5],'b':[1,34,56,77,8]}

# a=pd.Series(data,index=['a','b'],dtype=int,copy=True)

# print(a)

# data={'a':1,'b':2,'c':3}
# a=pd.Series(data)
# print(a)

# print(a.head(2))
# print(a.tail(3))

# print(a.ndim)
# print(a.values)
# print(a.axes)
# print(a.size)
# print(a.sha)


# print(a[['a','b','c']])

# print(a['a':'c'])



# data={'a':[1,2,3,4,5],'b':[1,34,56,77,8]}

# a=pd.Series(data,index=['a','b'],dtype=int,copy=True)

# print(a)

# print(a[['a']][1])



# data=[1,2,3,4,5,6,7]


# a=pd.Series(data)

# print(a[1:4])


# data=[[1,2,3],[4,5,6]]


# a=pd.DataFrame(data,columns=['a','b','c'])

# print(a)

# print(a[:])
# print(a['a'])


# data={'a':[1,2,3],'b':[4,5,6]}


# a=pd.DataFrame(data)

# print(a)

# import pandas as pd


# data=[{'a':1,'b':2},{'a':5,'b':5,'c':6}]


# a=pd.DataFrame(data)

# print(a['a'])




# import pandas as pd

# data ={
#     'one':pd.Series([1,2,3],index=['a','b','c']),
#     'two':pd.Series([1,2,3,4],index=['a','b','c','f']),
#     'two':pd.Series([1,2,3,4,5],index=['a','b','c','f','g'])
# }


# df=pd.DataFrame(data)

# print(df['one']>2)



# print(df[df['one']>2])

# print(df)

# print(df['one'])

# print(df['two'])

# print(type(df[['one','two']]))

# print(type(df['one']))


# import pandas as pd

# data ={
#     'one':pd.Series([1,2,3],index=['a','b','c']),
#     'two':pd.Series([1,2,3,4],index=['a','b','c','f'])
# }
   


# df=pd.DataFrame(data)

# df['three']=pd.Series([1,2,3,4],index=['b','c','d','f'])

# df['four']=pd.Series({'a':[1,2,3,4,5],'b':[2,4,455,66]})
# df['five']=df['one']+df['two']
# print(df)

# # del df['four']
# df.pop('four')

# print(df)



# print(df)

# print()

# print(df.loc['a':'f':2])

# print(df.iloc[0])




# import pandas as pd

# data ={
#     'one':pd.Series([1,2,3],index=['a','b','c']),
#     'two':pd.Series([1,2,3,4],index=['a','b','c','d'])
# }
   


# df=pd.DataFrame(data)
# df1=pd.DataFrame(data)
# print(df)
# print(df[1:])

# print(df[1:3])
# print(df[-1:])
# print(df[:-1])

# print(df[1:4:2])

# print(df[::])

# df2=df.append(df1)
# print(df2)



# import pandas as pd

# data=[[1,2,3],[4,5,6]]

# data1=[[7,8,9],[10,11,12]]
# df1=pd.DataFrame(data,index=[0,2],columns=['col1','col2','col3'])
# df2=pd.DataFrame(data1,index=[1,4],columns=['col1','col2','col3'])
# df=df1.append(df2)

# print(df)

# print(df.drop(0))

# import pandas as pd

# d={
#     'Name':pd.Series(['tom','james','nik','smith','john','don','rocky',5]),
#     'Age':pd.Series([23,24,25,26,27,23,23,9]),
#     'Rating':pd.Series([3.7,3.6,2.4,3.7,1.2,5.6,2.3,0])


# }

# df=pd.DataFrame(d)
# print(df)


# print(df.T)

# print(df.mode())

# print(df.ndim)
# print(df.size)

# print(df.shape)
# print(df.values)
# print(df.dtypes)

# print(df.empty)
# print(df.head(5))
# print(df.tail(5))


# import pandas as pd

# d={
#     'Name':pd.Series(['tom','james','nik','smith','john','don','rocky']),
#     'Age':pd.Series([23,24,25,26,27,23,23]),
#     'Rating':pd.Series([3.7,3.6,2.4,3.7,1.2,5.6,2.3])


# }

# df=pd.DataFrame(d)
# print(df)

# print(df.columns)
# print(df.max())
# print(df.min())
# print(df.axes)

# print(df.std())

# print(df.mean())
# print(df.median())
# print(df.mode())
# print(df.describe())

# print(df.cumsum())





# import random


# Clues=['Incorrect answer!!,try between 10 and 20','Wrong!!,Total digit sum is 5,try for it!!','Not the answer!!Try below 15']

# Cng=['Congratulations!!!You are a genius!!!','Wow!!!!You are awesome!!!!','Unbelievable!!!,Correct Answer!!','Right answer!!']

# Your_Guess=int(input('Enter a number :'))
# Answer=14


# if Your_Guess!=Answer:
#     print(random.choice(Clues))
# else:
#     print(random.choice(Cng))