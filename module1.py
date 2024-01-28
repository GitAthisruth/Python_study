# import datetime
# import time

# print(time.time())

# print(time.localtime(time.time()))
# mon=0
# tue=1
# print(time.asctime())


#we can make our on time
# tuple1=(1990,6,8,9,5,0,0,0,0)
# print(time.localtime(time.mktime(tuple1)))

# import timeit
# #this module used to calculate the time taken to execute this program

# print(timeit.timeit('[int(x)for x in [2.3,4.5,6.7]]'))

# from time import sleep
# sleep(5)
# print('Hello!!!!')

#calender 

# import calendar

# print(calendar.calendar(2027))
# print(calendar.isleap(2000))
# print(calendar.leapdays(1996,2024)
# print('Leap days between 1996 and 2024 is',calendar.leapdays(1996,2024))

#month(year,month,w,l)

# print(calendar.month(1997,10))
# print(calendar.month(1997,10,1,2))

# print(calendar.weekday(1997,10,21))
# print(help(calendar))
# print(help(time))
# print(dir(time))

# import datetime

# print(datetime.date(2022,4,5))

# dt=datetime.date(2022,4,5)
# print('Rahul was born in',dt)
# print(dt.year)
# print(dt.month)
# print(dt.day)

# print(datetime.date.today())
# dt=datetime.date.today()
# print(dt.weekday())
# print(dt.isoweekday())

# dt=datetime.date.today()
# td=datetime.timedelta(days=9)
# print(dt-td)

# dt=datetime.date.today()
# td=datetime.timedelta(days=9)
# print(dt+td)

# help(datetime)

# import random

# value=random.random()
# print(value)

#function random generate random decimal value between 0 and 1 each time it execute

# values=random.uniform(1.5,10.7)
# print(values)
#uniform can use two arguments that will print random values between that arguments
#arguments can be a integer value or float value
# value=random.randint(1,10)
# print(value)
#randint will print random values including 1 and 10

# values=['red','blue','black','green','orange','yellow']
# v=random.choice(values)
# print(v)
#choice will return only one value 

# values=['red','blue','black','green','orange','yellow']
# v=random.choices(values,k=2)
# print(v)

# choices will return more than one list of values

# values=['red','blue','black']
# v=random.choices(values,weights=[20,20,2],k=2)
# print(v)
#weights values decide which arguments to print based on its values argument with high value has high priority

# values=['hi','hai','hello']
# v=random.choice(values)
# print(v,'athisruth')

# a=list(range(1,20))
# random.shuffle(a)
# print(a)
#shuffle will print the random values of all given list values

# a=list(range(1,20))
# v=random.sample(a,k=5)
# print(v)
#sample will print 5 random list of values

#use case one

#random lottery pick
# from time import sleep
# import random
# lottery_tickets=[]
# print('Creating 100 tickets....')
# sleep(5)
# for i in range(100):
#     lottery_tickets.append(random.randrange(10000,99999))
# #randrange only return one value
# v=random.sample(lottery_tickets,k=2)
# print('Finding winners!!!! Please Wait')
# sleep(5)
# print('The winners are {}'.format(v))

# import random

# first_name=['Tuco','Melbin','Gustavo','Walter','Saul','Jesse']
# last_name=['Salamanga','Varghese','Fring','Walter','Goodman','Pinkman']
# street_name=['high','lose','low','hola','warks','rody']
# states=['Al','KL','ML','CP','EK','DL']
# fake_cities=['Mexico City','Amarakuni','Pulpally','Florida','Texas','Las Vegas']

# for i in range(6):
#     first=random.choice(first_name)
#     last=random.choice(last_name)
#     phone='{} --555--{}'.format(random.randint(100,999),random.randint(100,999))
#     street=random.choice(street_name)
#     state=random.choice(states)
#     city=random.choice(fake_cities)
#     zipcode=random.randint(100000,999999)
#     address='{} {} {} {}'.format(zipcode,street,city,state)
#     email=first+last+'@fakemail.com'
#     print('Name:{} {}\n{}\n{}\n{}'.format(first,last,phone,email,address))

#####################################################################
#dunder or magic method

#using this we can identify which modules that  we are currently working with
# print(__name__)

#####################################################################

# x=isinstance(5,int)#checking 5 is an integer.
# print(x)

#Instance is an object that belongs to a class. 
# For instance, list is a class in Python.
# When we create a list, we have an instance of the list class.
#object is a thing that can used to store a data and use it for other purpose.

# a=isinstance('ab',(int,str,float,list,dict,tuple))
# print(a)

# class myclass:
#     def hi(self,x):
#         print(x)
# obj1=myclass()
# obj1.hi('4')

# a=isinstance(obj1,myclass)##here checking obj1 is an object(instance) of class myclass
# print(a)

#######################################


# any 
# all

# a=[False,True,False,True]#any-checking any of the value is true here.
#print(any(a))
# a=[False,False]
# print(any(a))

# a=[False,True,True]#all-checking all of the value is true here.
# print(all(a))


# a=-11

# print(abs(a))#abs return the magnitude of a real number without regard to its sign.ie,a real number without its negative sign.

# a=-.2

# print(abs(a))