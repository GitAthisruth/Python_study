# def call():
#     print('Hi I am Athisruth')
# call()    

# def call():
#     a=[]
#     for i in range(1,8):
#         a.append(2**i)
#     print(a)
# call()

# def call(a=4,b=6):
#     sum=a+b
#     print(sum)
# call(a,b)    

# a=int(input('enter a value: '))
# b=int(input('enter a value: '))
# def call(a,b):
#     sum=a+b
#     print(sum)
# call(a,b)
#####################  
# def get():
#     add()
# def me():
#     get()    
# def add():
#     sum=6+5
#     print(sum)
# me()

########################
# def avrg(val):
#     sum=0
#     for i in range(val):
#         new=(int(input('Enter the values: ')))
#         sum=sum+new
#     avg=sum/val
#     print(avg)
# val=int(input('Enter the count: '))
# avrg(val)

# name1='Athisruth'
# name2='Todd'
# def callname():
#     name=name2
#     print('hi i am {} and this is {}'.format(name1,name))
#     def call(val):
#         Name='Dainty'
#         print('Hi this is {},he is {}'.format(Name,val))
#     call('awesome')    
# callname()  

#############################################################################

# def avg(n1,n2,n3):
#     return (n1+n2+n3)/3
# res1=avg(1,2,3)
# res2=avg(4,5,6)
# res3=avg(7,8,9)

# print(res1)
# print(res2)
# print(res3)

# def add(a,b):
#     return a+b
# print(add(2,3)) 

# def call():
#     a=[1,2,3,4]
#     c=0
#     for i in a:
#         c=c+i
#     return c
# res=call()
# print(res)    
    
# res = call()
# print(res)

# def add(a=1,b=2):
#     res=a+b
#     print(res)
# add()

# def add(a,b):
#     res=a-b
#     print(res)
# add(100,45)

# def add(a=1,b=2):
#     res=a+b
#     print(res)
# add(1,3)

# def add(a=1,b=2):
#     res=a+b
#     print(res)
# add(3)

# def add(*a):
#     c=[]
#     for i in a:
#         c.append(i)
#     print(c)
# add(1,2,3,4,5)
# 

# def val(a,*b):
#     A=a
#     for i in b:
#         A=A+i
#     print(A)
# val(1,2,3,4,5)  


# def vales(**val):
#     print(val)
#     for k,v in val.items():
#         print(k,v)
# vales(a='Walter',b='Jesse',c='Tuco') 

####################


# def fact(n):
#     f=1
#     if n<0:
#         return 'fact not support the negative numbers'
#     elif n==0:
#         return 'fact of zero is one'
#     else:
#         for i in range(1,n+1):
#             f=f*i
#         return 'fact of the {} is {}'.format(n,f)
# res = fact(int(input('Enter the number: ')))
# print(res)

#############

# def vals(x,y):
#     temp=x
#     x=y
#     y=temp
#     print('value of x is: ',x)
#     print('value of y is: ',y)
# x=8
# y=9
# vals(x,y)

# def iseven(n):
#     if n%2==0:
#         print('even')
#         return True
#     return False
# print(iseven(10)) 
# print(iseven(7))
# iseven(3)
# print(iseven(1))
#######################

# def val(n):
#     a=[]
#     for i in n:
#         if i%2==0:
#             a.append(i)
#     return a
# values=val([23,3,45,67,66,89,88,24])
# print(values)

######################
# def add():
#     a=float(input('Enter first number: '))
#     b=float(input('Enter second number: '))
#     return a+b
# sum=add()
# print(sum)
#######################
#lamda
##############
# a=lambda x,y,z:x*y*z
# print(a(2,3,3))

# def sum(a,b):
#     res=a+b
#     return res
# k=sum(3,6)
# print(k)

# w=lambda x,y:x+y
# print(w(3,6))

# q=(lambda a,b:a+b)(3,6)
# print(q)

# a=lambda x,y:x if x>y else y
# print(a(9,10))

# s=['Walter','Jesse','Mike','Gustavo']
# s.sort(key=lambda s:len(s))
# print(s)

# def val(a):
#     return (lambda x,y:(x*a)+y)(2,2)
# print(val(6))
#############################
# a=[2,3,4,5,6]
# num=[]
# sqr=lambda x:x**2
# for i in a:
#     num.append(sqr(i))
# print(num)
#################
# sqr=lambda x:x**2
# print(sqr(2))
########################
# def func(v=2):
#     c=v*2
#     return c
# high=lambda x,func:x+func
# print(high(3,func()))
###################3####
# high = lambda x,func:x+func
# print(high(3,5)) 
##############################
#function composition

# def add(x):
#     return x+2

# def mul(x):
#     return x*2

# print('adding 2 to 5 and multiplying with 2',mul(add(5)))
################################

# def compofunc(f,g):
#     return (lambda x:f(g(x)))(5)
# def add(x):
#     return x+2
# def mul(x):
#     return x*2
# def sub(x):
#     return x-2
# add_mul_sub_div=compofunc(compofunc(add,mul),sub)  
# print('''adding 2 to 5,then substracting 1 and 
# multiplying the result with 2''')

#########################################   

#recursive function
########################

# def fact(num):
#     if num==1:
#         return num
#     else:
#         return num*fact(num-1)

# num1=int(input('enter the number: ')) 
# if num1<0: 
#     print('not allowed')
# elif num1==0:
#     print('fact for zero is 1')
# else:print('fact of {} is {} '.format(num1,fact(num1)))  
############################

# def list_sum(num):
#     if len(num)==1:
#         return num[0]
#     else:
#         return num[0] + list_sum(num[1:])
# print(list_sum([2,3,4,5]))  
##############################################
# def lssum(data):
#     total =0
#     for val in data:
#         if type(val)==type([]):
#             total=total + lssum(val)
#         else:
#             total =total+val
#     return total
# print(lssum([1,2,[3,4],[5,6]]))  
##################################
#enumerate function
##########################

# vals=['red','blue','black']
# for i in range(len(vals)):
#     print(i,vals[i])    

# vals=['red','blue','black']
# a=[]
# for k,i in enumerate(vals):
#     a.append(k)
# print(a)
#########################################################
#map,reduce,filter
#########################################################
#map
#map(function,sequence)
######################
# def sqr(b):
#     return b*b
# b=[2,3,4]
# print(sqr(b))
# print(list(map(sqr,[2,3,4])))

# b=[2,3,4]
# print(list(map(lambda x:x*x,b)))

# b=[2,3,4]
# c=[5,6,4]
# d=[1,8,7]
# print(list(map(lambda x,y,z:x+y+z,b,c,d)))
#####################
#filter
#####################

# for i in range(1,11):
#     if i%2==0:
#         print(i)
#####################
#filter(function,Iterable)
#filter will filter the unwanted values

# print(list(filter(lambda x:x%2==0,range(1,11))))
# print(tuple(filter(lambda x:x%2==0,range(1,11))))
# print(filter(lambda x:x%2==0,range(1,11)))

#reduce


# import functools
# num=[1,2,3,4]
# a=functools.reduce(lambda x,y:x+y,num)
# print(a)



