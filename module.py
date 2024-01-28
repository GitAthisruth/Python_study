# import datetime
# import time

# print(time.time())
# #time() The time() function returns the number of seconds passed since epoch.
# #The epoch time, also known as POSIX time, Unix time, and Unix timestamp, 
# #indicates the number of seconds passed since 1st January 1970, excluding the leap seconds
# print(time.localtime(time.time()))

#localtime() The localtime() function takes the number of seconds passed since epoch as an argument and returns struct_time in local time.
# mon=0
# tue=1
# print(time.asctime())
# #converts a tuple or struct_time 
# #representing a time as returned by gmtime() or localtime() to a 24-character string 


# #we can make our on time
# tuple1=(1990,6,8,9,5,0,0,0,0)
# print(time.localtime(time.mktime(tuple1)))

# s=time.localtime(time.mktime(tuple1))
# print(time.asctime(s))

# import timeit
# # #this module used to calculate the time taken to execute this program

# print(timeit.timeit('[int(x) for x in [2.3,4.5,6.7]]'))

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

# #To create a date, we can use the datetime() class (constructor) of the datetime module
# dt=datetime.date(2022,4,13)
# # print('Rahul was born in',dt)
# print(dt.year)
# print(dt.month)
# print(dt.day)

# print(datetime.date.today())
# dt=datetime.date.today()
# print(dt.weekday())
# print(dt.isoweekday())
#An ISO week-numbering year has 52 or 53 full weeks. Week 1 is defined to be the first week with 4 or more days in January

# dt=datetime.date.today()
# td=datetime.timedelta(days=9)
#Python timedelta() function is present under datetime library 
# which is generally used for calculating differences in dates and also can be used for date manipulations in Python
# print(dt-td)

# dt=datetime.date.today()
# td=datetime.timedelta(days=9)
# print(dt+td)

# help(datetime)

##############################################################

# Python code to demonstrate the working of
# asctime() and ctime()

# importing "time" module for time operation
# import time

# # initializing time using gmtime()
# ti = time.gmtime()

# # using asctime() to display time acc. to time mentioned
# print ("Time calculated using asctime() is : ",end="")
# print (time.asctime(ti))


# using ctime() to display time string using seconds
# print ("Time calculated using ctime() is : ",end='')
# print (time.ctime())



#############################################################################
#dunder or magic method
# print(__name__)

##############################################################################

# x=isinstance(5,int)
# print(x)

# x=isinstance('a',(int,str,float,list,dict,tuple,complex))
# print(x)

# x=isinstance(complex(2,3),(int,str,float,list,dict,tuple,complex))
# print(x)

# a=complex(2,3)
# print(a)

# class myclass:
#     def hi(self,x):
#         print(x)

# obj1=myclass()
# obj1.hi('heloo')

# b=isinstance(obj1,myclass) 
# print(b)

######################################
# any
# all

# a=[True,False]
# print(any(a))

# a=[False,False]
# print(any(a))

# a=[True,True]
# print(all(a))