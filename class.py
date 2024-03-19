#Object Oriented Programming(OOP) with python



#class and instances
#class and variables
#class method and static method
#inheritance -> creating subclass
#special method ->(magic/dunder methods)
#property decorators - getter,setter and deleter

# class employee():
#     pass
# emp1=employee()#here we create an object
# print(emp1)


############MANUAL METHOD###############

# class Employee(): #class is the keyword    
#     pass
# emp1=Employee()# epm1 is the object of the class called Employee
# emp1.first="devin"
# emp1.last="mathew"
# emp1.email="devin@gmail.com"
# emp1.pay=50000
# print(emp1)#Here print object


# emp2=Employee()# epm2 is the another object of the class called Employee
# emp2.first="david"
# emp2.last="wilson"
# emp2.email="david@gmail.com"
# emp2.pay=40000
# print(emp2)

# print(emp1.first)
# print(emp2.first)
# print(emp1.first)




#######automated method########


#Class  - Class is a logical structure.

#Object - Object is a physical entity.We set  parameters to objects.Object contains the  class with arguments replaced by parameters.That is called it is a physical entity.

#We can only create an object after creating a class,that is called a class is a blue print of an object.

# class tuco():
#     def __init__(self,first,last,num):#__init__ is a member function
#         self.first=first
#         self.last=last
#         self.mail=first+'.'+last+'@gmail.com'
#         self.num=num
        

# t1=tuco('Tuco','Salamanga',9876521090)


# print(t1.first)
# print(t1.last)
# print(t1.mail)
# print(t1.num)
# print(t1.__doc__)



    
#     def ssm(self,name3):
        # self.name3=name3

# print(Person.age)   

# print(Person.greet)

# print(Person.__doc__)

# create a new object of Person class# 
# class Person():
#       "This is a person class"
#       age=10
#       def __init__(self,name34,name0,name2):
#           self.name34=name34
#           self.name0=name0
#           self.name2=name2
#       def greet(self):
#            return self.name0 + self.name2
#       def sm(self):
#            return self.name2 * self.name34 

# p=Person(34,67,45)
# print(p.name34)
# print(p.name0)
# print(p.name2)

# print(p.greet())
# print(p.sm())



# Harry=Person()


# Harry.greet()
# Harry.sm('harry')
# print(Harry.greet)

# Harry.greet()#calling object's greet() method


# class Person():
        #"This is a person class"
#     def __init__(self,name34,name0,name2):
#         self.name34=name34
#         self.name0=name0
#         self.name2=name2
#     age=10
#     def greet(self):
#         # self.name0=name0
#         # self.name2=name2
#         # print("Hello")
#         print(self.name0 + self.name2)
#     def sm(self):
#         print(self.name2  * self.name34)

# p=Person(6,7,8)
# p1=Person(9,10,11)

# p.greet()
# p.sm()
# p1.greet()
# p1.sm()


# class Person():
#     #"This is a person class"
#     def greet(self,name0):
#         self.name0=name0
#         # self.name0=name0
#         # self.name2=name2
#         # print("Hello")
#         print(self.name0)
#     def sm(self,name2):
#         self.name2=name2
#         print(self.name2)

# p=Person()
# p1=Person()

# p.greet('45')
# p.sm('78')
# p1.greet('23')
# p1.sm('43')



# class Gustavo():
#     pass
# a=Gustavo()
# a1=Gustavo()
# a.first='Gustavo'
# a.last='fring'
# a.mail='gustavofring@gmail.com'
# a.phone='9857390187'


# a1.first='Jesse'
# a1.last='Pinkman'
# a1.mail='Pinkmang@gmail.com'
# a1.phone='9887390887'

# print(a.first)
# print(a1.first)


# class Tuco():
#     def __init__(self,first,last,num):
#         self.first=first
#         self.last=last
#         self.mail=first + '.'+last+'@gmail.com'
#         self.num=num
#     def Jesse(self):
#         print(self.first+' '+self.last)

# t=Tuco('Jesse','Pinkman','7034204128')
# t.Jesse()
# print(t.first)

# class Tuco():
#     'Hi I am Tony'
#     def __init__(self,first,last,num):
#         self.first=first
#         self.last=last
#         self.mail=first + '.'+last+'@gmail.com'
#         self.num=num
#     def Jesse(self):
#         return self.first+' '+self.last

# t=Tuco('Jesse','Pinkman','7034204128')
# print(t.Jesse())
# print(t.first)

# print(t.__doc__)#__doc__ used to print a string after the class function



# t=Tuco()
# t.sm('Jesse')
# t.ss('Pinkman')
# print(t.first)
# print(t.last)

# t.Jesse()

#################################################################

# class employee():
#       def __init__(self,first,last,pay):#__init__ is  initialization.
#           self.first=first
#           self.last=last
#           self.mail=first+'.'+last+'@company.com'
#           self.pay=pay

# emp1=employee('Devin','Mathew',10000000)
# emp2=employee('Rahul','Krishna',5000000)
# emp3=employee('Alex','Mathew',10000000)

# print()
# print(f'{emp1.first} {emp1.last}')
# print()
# print(f'{emp2.first} {emp2.last}')
# print()
# print(f'{emp3.first} {emp3.last}')

#we can call this function in another way

# class employee():
#       def __init__(self,first,last,pay):#__init__ is  initialization.
#           self.first=first
#           self.last=last
#           self.mail=first+'.'+last+'@company.com'
#           self.pay=pay
#       def full(self):
#            return f"{self.first} {self.last}\n{self.mail}\n{self.pay}"

# emp1=employee('Devin','Mathew',10000000)
# emp2=employee('Rahul','Krishna',5000000)
# emp3=employee('Alex','Mathew',10000000)

# print()
# print(emp1.full())
# print()
# print(emp2.full())
# print()
# print(emp3.full())
# print()

# print(employee.full(emp1))#this is the another way to call the fuction

# class employee():
#       def __init__(self,first,last,pay):#__init__ is  initialization.
#           self.first=first
#           self.last=last
#           self.mail=first+'.'+last+'@company.com'
#           self.pay=pay
#       def full(self):
#            return f"{self.first} {self.last}\n{self.mail}\n{self.pay}"

# emp1=employee('Devin','Mathew',10000000)
# emp2=employee('Rahul','Krishna',5000000)
# emp3=employee('Alex','Mathew',10000000)

# val=[emp1,emp2,emp3]
# for i in val:
#         print(i.full(),'\n')


# class employee():
#       def __init__(self,first,last,pay):#__init__ is  initialization.
#           self.first=first
#           self.last=last
#           self.mail=first+'.'+last+'@company.com'
#           self.pay=pay*1.04 #here the change will affect to all employees
#       def full(self):
#            return f"{self.first} {self.last}\n{self.mail}\n{self.pay}"

# emp1=employee('Devin','Mathew',10000000)
# emp2=employee('Rahul','Krishna',5000000)
# emp3=employee('Alex','Mathew',10000000)

# print(emp1.full())

# class employee():
#       def __init__(self,first,last,pay):#__init__ is  initialization.this is the dunder/magic method.
#           self.first=first
#           self.last=last
#           self.mail=first+'.'+last+'@company.com'
#           self.pay=pay
#       def full(self):

#               return f"{self.first} {self.last}\n{self.mail}\n{self.pay}"
#       def payment(self):
#               return f'{self.pay*1.05}'#here we can see separately the incremented salary and normal salary of each employees.

# emp1=employee('Devin','Mathew',10000000)
# emp2=employee('Rahul','Krishna',5000000)
# emp3=employee('Alex','Mathew',10000000)

# print(emp1.payment())
# print()
# print(emp1.full())


# class employee():

        
#         def __init__(self,first,last,pay):#__init__ is  initialization.
#           self.first=first
#           self.last=last
#           self.mail=first+'.'+last+'@company.com'
#           self.pay=pay
#         def full(self):
#                return f"{self.first} {self.last}\n{self.mail}\n{self.pay}"
#         def increment(self):
#                return f"{self.first} {self.last}\n{self.mail}\n{self.pay*1.04}"

# emp1=employee('Devin','Mathew',10000000)
# emp2=employee('Rahul','Krishna',5000000)
# emp3=employee('Alex','Mathew',10000000)

# print(emp1.full())
# print()
# print(emp1.increment())


# class employee():
#       empval=1.06  #here we can  seperately increment the salary of particular employees.empval is a class variable and act as a global variable.
#       def __init__(self,first,last,pay):#__init__ is  initialization.
#           self.first=first
#           self.last=last
#           self.mail=first+'.'+last+'@company.com'
#           self.pay=pay
#       def full(self):
#                return f"{self.first} {self.last}\n{self.mail}\n{self.pay}"
#       def increment(self):
#            return f"{self.first} {self.last}\n{self.mail}\n{self.pay*self.empval}"

# emp1=employee('Devin','Mathew',10000000)
# emp2=employee('Rahul','Krishna',5000000)
# emp3=employee('Alex','Mathew',10000000)

# print(emp1.full())
# print()
# print(emp1.increment())

# print(emp1.__dict__)#here we can call all values in emp1 as a dict format.








# class employee():
#       empval=1.06  
#       def __init__(self,first,last,pay):#__init__ is  initialization.
#           self.first=first
#           self.last=last
#           self.mail=first+'.'+last+'@company.com'
#           self.pay=pay
#       def nonincre(self):
#            return f"{self.first}\n{self.last}\n{self.mail}\n{self.pay}"
#       def increment(self):
#            return f"{self.first} {self.last}\n{self.mail}\n{self.pay*self.empval}"


# emp1=employee('Devin','Mathew',10000000)
# emp2=employee('Rahul','Krishna',5000000)
# emp3=employee('Alex','Mathew',10000000)


# print(emp1.nonincre())
# print()
# print(emp1.increment())


# class employee():
#       empval=1.06  
#       def __init__(self,first,last,pay):#__init__ is  initialization.
#           self.first=first
#           self.last=last
#           self.mail=first+'.'+last+'@company.com'
#           self.pay=pay
#       def nonincre(self):
#            return f"{self.first} {self.last}\n{self.mail}\n{self.pay}"
#       def increment(self):
#            return f"{self.first} {self.last}\n{self.mail}\n{self.pay*self.empval}"


# emp1=employee('Devin','Mathew',10000000)

# emp2=employee('Rahul','Krishna',50000000)

# emp3=employee('Alex','Mathew',10000000)



# print(emp1.nonincre())
# print()
# print(emp1.increment())


# emp1.empval=1.06 #here we can seperately assign different values to the variable empval,it only affect the given object.
# #other objects only assign the class variable that already given.
# emp3.empval=1.08
# print(emp1.increment())
# print()
# print(emp2.increment())
# print()
# print(emp3.increment())


# print(emp3.__dict__)
# print(employee.__dict__)#here we get all the elements and instance variables of the class employee as dict format.


# class employee():
#         "this is employee class"#we should always mention the string in the begining.otherwise we get a result as none.
#         empval=1.06  
#         def __init__(self,first,last,pay):#__init__ is  initialization.
#           self.first=first
#           self.last=last
#           self.mail=first+'.'+last+'@company.com'
#           self.pay=pay
#         def nonincre(self):
#                 'this is a class method'
#                 return f"{self.first} {self.last}\n{self.mail}\n{self.pay}"
#         def increment(self):
#                 return f"{self.first} {self.last}\n{self.mail}\n{self.pay*self.empval}"


# emp1=employee('Devin','Mathew',10000000)

# emp2=employee('Rahul','Krishna',50000000)

# emp3=employee('Alex','Mathew',10000000)

# print(employee.__doc__)

# print(employee.nonincre.__doc__)

# print(emp1.__class__)

#################################################################



#first class function

# def square(x):
#         return x*x

# square(5)

# f=square#here is assigning function name to another variable and calling the function using it,that is called first class function.

# print(f(4))


################################################################

#Higher order function

# def square(x):
#         return x*x

# def cube(x):
#         return x*x*x

# def mymap(func,arg):#here we assign the square function to the argument func,the func=square function.
#         my_ls=[]
#         for i in arg:
#             my_ls.append(func(i))
#         return(my_ls)

# val=mymap(square,[1,2,3,4])
# print(val)


# def m(f,k):
#         my=[]
#         for i in k:
#                 my.append(f(i))
#         return(my)


# val=m(cube,[2,3,4])
# print(val)

###############################################################

# def logger(x):#we can still access the inner function if the outer(main) function execution  completed.inner function can access the outer function variables at anytime.
#         def log_msg():
#                 print('msg:',x)
#         return log_msg

# val=logger('Hii')
# print(val.__name__)
# val()


######################################################################

# def html_tag(tag):
#         def wrap_text(msg):
#                 print(f'<{tag}> <{msg} </{tag}>')
#         return wrap_text
# val=html_tag('hi')
# val('first line')

#####################################################################

# closure


# def outer_function():
#         msg='Hello'
#         def inner_func():#here the outer function variable is access by the inner function after the outer function execution completed.
#                 print(msg)
#         return inner_func
       
# val=outer_function()
# val()


#######################################################################

#Decorators #

# def decorator_function(original_function): #inner function return the outer function and outer function return the inner function name.
#         def wrapper_function():
#                 print(f"wrapper executed before the {original_function.__name__}")
#                 return original_function()   #here exactly calling the display function.
#         return wrapper_function      #here we just call the function name 


# def display():
#         print('display function executed')


# wrapped=decorator_function(display)#we assign display function as argument here.
# print(wrapped.__name__)#<variablename>.__name__  mention the name of the  data currently  carrying in the <variablename>.
# wrapped()


#############################################################################################################

# def b(c):
#         def d():
#                 print('my name is ',c.__name__)
#                 print(c())

#         return d

# def a():
#         return 'hi i am tony'



# v=b(a)
# print(v.__name__)
# v()

###################################################################################################

# def decorator_function(original_function): #inner function return the outer function and outer function return the inner function name.
#         def wrapper_function():
#                 print(f"wrapper executed before the {original_function.__name__}")
#                 return original_function()   #here exactly calling the display function.
#         return wrapper_function      #here we just call the function name 





# @decorator_function #This is the decorator #Here we calling the display function through the main function-decorator_function.
#                     #here display function move as an argument to the main function.Here last execution is the returning the original_function(ie,original function = display function only inside the function we can't call it outside the function).
#                     #then all value pass to the display function.
# def display():
#         print('display function executed')


# display()#when we call the display function the name display move as an argument to the main function.(when we give return and print function then we can use print function to call the function)




##############################################################################################


# def decorator_function(original_function): #inner function return the outer function and outer function return the inner function name.
#         def wrapper_function(*args,**kwargs): #*args(eg-name,age) is the arguments and **kwargs(eg-name='alex',age=8) we need to give both arguments as a standard way to avoid error.
#                 #here we need to store the arguments in inner function also.because we are calling the display_info function.
#                 print(f"wrapper executed before the {original_function.__name__}")
#                 return original_function(*args,**kwargs)   #here exactly calling the display function.
#         return wrapper_function      #here we just call the function name 




# @decorator_function #This is the decorator #Here we calling the display function through the main function-decorator_function.
#                     #here display function move as an argument to the main function.
#                     #here we not need to seperately give variable names and arguments.

# def display():
#         print('display function executed')

# def display_info(name,age,place):
#         print(f'display function ran with arguments {name} {age} {place}')


# display()
# display_info('Jesse',29,'New Mexico')


###################################################################################################################

# def ab(ba):
#         def bn(*an,**am):
#                 print(f'print {ba.__name__}')
#                 return ba(*an,**am)

#         return bn

# @ab

# def p():
#         print('Yo!!Man!!Whatsupp!!')
# def a(a,b,c):

#         print(f'here print {a},{b},{c}')

# p()
# a(3,4,5)


################################################################


# import time


# def calctime_square(numbers):
#         start=time.time()
#         res=[]
#         for number in numbers:
#                 res.append(number*number)
#         end=time.time()
#         print('calc square tool:'+ str((end-start)*1000)+'mil sec')
#         # print('calc square tool:',end-start,'mil sec')   #Concatenation means joining strings together end-to-end to create a new string. To concatenate strings, we use the + operator. 
#         #Keep in mind that when we work with numbers, + will be an operator for addition, but when used with strings it is a joining operator.
#         return res

# # print(calctime_square(range(1,100000)))
# # calctime_square(range(1,100000))


# def calctime_cube(numbers):
#         start=time.time()
#         res=[]
#         for number in numbers:
#                 res.append(number*number*number)
#         end=time.time()
#         print('calc cube tool:'+ str((end-start)*1000)+'mil sec')


# array=range(1,10000)
# square=calctime_square(array)
# cube=calctime_cube(array)


##############################################################################################



# import time


# def time_it(func):
    
#     def wrapper(*arg,**karg):#when the inner function will call the value array take to this wrapper function.
#         start=time.time()
#         calcti=func(*arg,**karg)#function call is happening here , after this function call the final result will pass to the function calctime_square.
#         end=time.time()
#         print(func.__name__ + ' took ' + str((end-start)*1000)+'mil sec')
#         return calcti #here the result is return to the function call.
#     return wrapper


# @time_it #using decorators is an easy way to check time of many programs easily.

# def calctime_square(numbers): #when we call it the  function name calctime_square will pass to func.
#         res=[]
#         for number in numbers:
#                 res.append(number*number)
#         return res


# @time_it
# def calctime_cube(numbers):
#         res=[]
#         for number in numbers:
                # res.append(number*number*number)
#         return res



# array=range(1,100000)
# calctime_square(array)#when we call it the  function name calctime_square will pass to func.
# calctime_cube(array)

##############################################################################################

# def decorator_function(original_function): #inner function return the outer function and outer function return the inner function name.
#         def wrapper_function(*args,**kwargs): #*args(eg-name,age) is the arguments and **kwargs(eg-name='alex',age=8) we need to give both arguments as a standard way to avoid error.
#                 #here we need to store the arguments in inner function also.because we are calling the display_info function.
#                 print(f"wrapper executed before the {original_function.__name__}")
#                 return original_function(*args,**kwargs)   #here exactly calling the display function.
#         return wrapper_function      #here we just call the function name 




# @decorator_function #This is the decorator #Here we calling the display function through the main function-decorator_function.
#                     #here display function move as an argument to the main function.
#                     #here we not need to seperately give variable names and arguments.

# def display():
#         print('display function executed')

# def display_info(name,age,place):
#         print(f'display function ran with arguments {name} {age} {place}')


# display()
# display_info('Jesse',29,'New Mexico')

###################################################################################################################

# class decorator_function(object):#giving object as an argument is a standard way.it used to work the __call__  properly.object is an inbuilt value.
#         def __init__(self,org_function):#init is a constructor
#                 self.org_function=org_function


#         def __call__(self,*arg,**kwargs):#call is a dunder/magic method.this method is used to call the function automatically.

#             print(f'wrapper executed before the {self.org_function.__name__}')
#             return self.org_function(*arg,**kwargs)





# @decorator_function #this is called class method.
# #A class method is a method that is bound to a class rather than its object.
# # It doesn't require creation of a class instance, much like staticmethod.
# # The difference between a static method and a class method is: Static method knows nothing about the class and just deals with the parameters.


# def display(*arg,**kwargs):
#         print('display function executed')

##############################################################################


# class sample:
#         value='This is the new value'#here value is a class variable

#         def __init__(self):
#             print('Hi Tuco')
        
#         def getvalue(self):
#                 value='This is the getvalue variable'#here value is a local variable
#                 print('The value is going to print is:',self.value)#here we call the class variable using self.<variablename>
#                 # print('The value is going to print is:',value)#local variable call without mentioning the self.



# sample()
# obj=sample()#here we call the class sample and automatically execute the init function.
# obj.getvalue()

# obj.value='UPDATED ONE'
# obj.getvalue()

###############################################################################################
#class method




# class employee:
#         empval=1.06
#         def __init__(self,first,last,pay):
#                 self.first=first
#                 self.last=last
#                 self.mail=first + '.' + last + '@gmail.com'
#                 self.pay=pay

#         def fullname(self):
#                 return '{} {}\n{}\n{}'.format(self.first,self.last,self.mail,self.pay)
#         def fullname1(self):
#                 return '{} {}\n{}\n{}'.format(self.first,self.last,self.mail,self.pay*self.empval)
#         def increment(self):
#             return '{}'.format(self.pay*self.empval)
        
#         @classmethod#this is how we use classmethod,here we assign a new value to the empval after replacing the old value..

#         def setraisement(cls,value):#here we changing 
#         #    employee.empval#value #here we can use both way
#             cls.empval=value#this is the standard way.
       



# emp1=employee('Devin','Mathew',10000000)

# emp2=employee('Rahul','Krishna',10000000)

# emp3=employee('Alex','Mathew',10000000)

# print(emp1.increment())
# print()
# print(emp2.increment())
# print()
# print(emp3.increment())
# print()





# employee.setraisement(1.07)#here we call the function setraisement then the value 1.07 pass to the value inside the class functin setraisement.
# #then empval value change to new value

# print(emp1.increment())
# print()
# print(emp2.increment())
# print()
# print(emp3.increment())
# print()


#####################################################################################################################

# class employee:
#         empval=1.06
#         def __init__(self,first,last,pay):
#                 self.first=first
#                 self.last=last
#                 self.mail=first + '.' + last + '@gmail.com'
#                 self.pay=pay

#         def fullname(self):
#                 return '{} {}\n{}\n{}'.format(self.first,self.last,self.mail,self.pay)
#         def fullname1(self):
#                 return '{} {}\n{}\n{}'.format(self.first,self.last,self.mail,self.pay*self.empval)
#         def increment(self):
#             return '{}'.format(self.pay*self.empval)
          
                  
#         @classmethod
#         def setraisement(cls,value):#here we changing 
#         #     employee.empval=value
#             cls.empval=value

#


# emp1=employee('Devin','Mathew',10000000)

# emp2=employee('Rahul','Krishna',10000000)

# emp3=employee('Alex','Mathew',10000000)

# str1='John-Gol-45000'
# str2='Don-Boss-65000'
# str3='Ram-Wilson-75000'

# first,last,pay=str1.split('-')#here the string str1 is going to split from this '-' and stored each value to first,last and pay
# #first=John,last=Gol,pay=45000
# # print(first)
# newobj=employee(first,last,pay)
# print()
# print(newobj.first,newobj.last,'\n',newobj.mail,'\n',newobj.pay)
# print()

# first,last,pay=str2.split('-')
# newobj1=employee(first,last,pay)
# print(newobj1.first,newobj.last,'\n',newobj.mail,'\n',newobj.pay)
# print()

# first,last,pay=str3.split('-')
# newobj=employee(first,last,pay)
# print(newobj.first,newobj.last,'\n',newobj.mail,'\n',newobj.pay)
# print()

#we need to call other strings seperately  by using these programs again annd again ,this method is very complex.


###################################################################################################################

# class employee:
#         empval=1.06
#         def __init__(self,first,last,pay):
#                 self.first=first
#                 self.last=last
#                 self.mail=first + '.' + last + '@gmail.com'
#                 self.pay=pay

#         def fullname(self):
#                 return '{} {}\n{}\n{}'.format(self.first,self.last,self.mail,self.pay)
#         def fullname1(self):
#                 return '{} {}\n{}\n{}'.format(self.first,self.last,self.mail,self.pay*self.empval)
#         def increment(self):
#             return '{}'.format(self.pay*self.empval)
          
                  
#         @classmethod
#         def setraisement(cls,value):#here we changing 
#         #     employee.empval=value
#             cls.empval=value

#         @classmethod
#         def setstr(cls,value):
#             first,last,pay=value.split('-')
#             return cls(first,last,pay) #cls representing the class employee.here we can use cls or employee.


# emp1=employee('Devin','Mathew',10000000)

# emp2=employee('Rahul','Krishna',10000000)

# emp3=employee('Alex','Mathew',10000000)

# str1='John-Gol-45000'
# str2='Don-Boss-65000'
# str3='Ram-Wilson-75000'

# newobj=employee.setstr(str1)#when we call it the classmethod will execute first and then the constructor will execute.

# print(newobj.first)
# print(newobj.last)
# print(newobj.mail)
# print(newobj.pay)

########################################################################################################################

#static method

#when we use a static method our new function(method) has no connection with the constructor(init) the method used with staticmethod has called seperately.
#This method not representing the main class.


# class employee:
#         empval=1.06
#         def __init__(self,first,last,pay):
#                 self.first=first
#                 self.last=last
#                 self.mail=first + '.' + last + '@gmail.com'
#                 self.pay=pay

#         def fullname(self):
#                 return f'{self.first} {self.last}\n{self.mail}\n{self.pay}'
#         def raiseamount(self):
#                 return f'{self.pay*self.empval}'
        
#         @staticmethod #here is the same effect that we call this fuction outside the function.but when we declare this type of function we should mention @staticmethod.
#         def findday(day):
#             if day.weekday() ==5 or day.weekday()==6: #here 5,6 representing saturday and sunday in a week,monday start with 0.
#                return "Yoo!!!Man!!Its Weekend!!!"
#             return "Oops!!Workday!!!!"
        


# import datetime
        
# mydate=datetime.date(2022,5,18)#(year,month,date)
# mydate1=datetime.date(2022,5,21)
# print(employee.findday(mydate))#when we call it argument mydate stored to day.
# print(employee.findday(mydate1))

# print(datetime.date.weekday(mydate))

# print("hi")


##################################################################################################################

#Abstract method 

#A class is called an Abstract class if it contains one or more abstract methods.
# An abstract method is a method that is declared, but contains no implementation.
# Abstract classes may not be instantiated, and its abstract methods must be implemented by its subclasses.
#normal function(method) is called regular method.

#here we use abstract method to deny the access of a particular method(function) in the class by other users.

# from abc import ABC,abstractclassmethod

# class shape(ABC):#here we inherit ABC to the class
        
#         @abstractclassmethod #here the abstractmethod is a decorator.
#         def area(self):#we should mention (self) here.
#                 print('This is area method')

#         def perimeter(self):
#                 print('This is Perimeter Method')
#         print('This is Shape Class')#this will execute automatically when we run the program because it is not inside a function(method) in the class.
        #class is not a function.


# class square(shape): #Here we inherit the main class name as argument inside the child class square.So, it can access the all methods and attributes of main class.
#         def __init__(self,side):
#             self.side=side
                
#         def area(self):
#             print(self.side*self.side)
        
#         def perimeter(self):
#             print(4*self.side)

# shape=square(6)
# shape.area()
# shape.perimeter()
# after calling the methods the access is denied due to the abstract method,
# But the print() function in the class still execute because abstract method is apply to the methods(function) of the class.
# also if we give a print function in the class it will execute automatically when we run.


################################################################################################################


#Inheritance

#Using inheritance method the main class name as argument inside the child class.So, it can access the all methods ,attributes and all other properties of main class(ie,the parent class).

# class employee:
#         empval=1.06
#         def __init__(self,first,last,pay):
#                 self.first=first
#                 self.last=last
#                 self.mail=first + '.' + last + '@gmail.com'
#                 self.pay=pay

#         def fullname(self):
#                 return f'{self.first} {self.last}\n{self.mail}\n{self.pay}'

#         def raiseamount(self):
#                 return f'{self.pay*self.empval}'

# class developer(employee):#here employee class act as a parent class and developer class is a child class of the employee class.
#       pass                     #here developer class can access all the properties of the parent class.

# dev=developer('tom','ward',78000) #here the arguments store to the first,last,pay in the order.

# print(dev.first)
# print(dev.last)
# print(dev.mail)
# print(dev.pay)
# print(dev.fullname())

################################################################################################################


# class employee(): #here no need to give the () symbol in the main class.
#         empval=1.06
#         def __init__(self,first,last,pay):
#                 self.first=first
#                 self.last=last
#                 self.mail=first + '.' + last + '@gmail.com'
#                 self.pay=pay

#         def fullname(self):
#                 return f'{self.first} {self.last}\n{self.mail}\n{self.pay}'

#         def raiseamount(self):
#             self.pay=self.pay*self.empval


# class developer(employee):
#       pass


# dev1=developer('tom','ward',78000)#dev1 is an object of class developer 

# print(dev1.pay)
# dev1.raiseamount()#after calling the raiseamount then the pay value  78000 change to new value and that value pass to the developer object and replace 78000.
# print(dev1.pay)#then we print the pay value again then we get the incremented value.


###########################################################################################################################

# class employee(): 
#         empval=1.06
#         def __init__(self,first,last,pay):
#                 self.first=first
#                 self.last=last
#                 self.mail=first + '.' + last + '@gmail.com'
#                 self.pay=pay

#         def fullname(self):
#                 return f'{self.first} {self.last}\n{self.mail}\n{self.pay}'

#         # @property
#         def raiseamount(self):
#             self.pay=self.pay*self.empval
#         #     return self.pay*self.empval
        
#         def newname(self):
#             self.first='dff'   


# class developer(employee):
#       empval=1.10
      


# dev1=developer('tom','ward',78000)
# dev2=employee('tom','ward',78000)
# print(dev2.raiseamount)

# print(dev1.pay)
# dev1.raiseamount()#after calling this method the empval value is taking from the developer class because the object we created is for the developer class.
# print(dev1.pay)


# dev2=developer('Sabu','Ravi',53636)

# print(dev2.pay)
# print(dev2.first)

# dev2.raiseamount()
# dev2.newname()
# print(dev2.pay)
# print(dev2.first)

####################################################################################################################


# class employee(): 
#         empval=1.06
#         def __init__(self,first,last,pay):
#                 self.first=first
#                 self.last=last
#                 self.mail=first + '.' + last + '@gmail.com'
#                 self.pay=pay

#         def fullname(self):
#                 return f'{self.first} {self.last}\n{self.mail}\n{self.pay}'

#         def raiseamount(self):
#             self.pay=self.pay*self.empval
        
        

# class developer(employee):
#       empval=1.10
#       def __init__(self,first,last,pay,prolng):
#           super().__init__(first,last,pay) #here super() method used to access the first,last,pay from the parent class because we already declare it.so we can add new arguments.
#           self.prolng=prolng               #here we want to add one more variable in the child class.so we do this method.

      


# dev1=developer('tom','ward',78000,'python')

# print(dev1.first)
# print(dev1.last)
# print(dev1.mail)
# print(dev1.pay)
# print(dev1.prolng)

###################################################################################################################

# class employee(): 
#         empval=1.06
#         def __init__(self,first,last,pay):
#                 self.first=first
#                 self.last=last
#                 self.mail=first + '.' + last + '@gmail.com'
#                 self.pay=pay

#         def fullname(self):
#                 return f'{self.first} {self.last}'
#         def raiseamount(self):
#             self.pay=self.pay*self.empval
        
        

# class developer(employee):
#       def __init__(self,first,last,pay,prolng):
#           super().__init__(first,last,pay) #here super() method used to access the first,last,pay from the parent class because we already declare it.so we can add new arguments.
#           self.prolng=prolng               #here we want to add one more variable in the child class.so we do this method.


# class manager(employee):
#       def __init__(self,first,last,pay,employees=None):#here we set a default value to employees as none,None is not same as False,None is not 0.Here we set employees=None to check conditions.
#                                                        #Here we can use other values like none(eg:employees=a string  or an int value.)
#                                                        #None is not an empty string,Comparing None to anything will always return False except none itself.
#           super().__init__(first,last,pay)        
#           if employees == None:                        #Here we can use employees == None(This not work in int ) or employees is None.
#              self.employees=[]
#           else:
#                self.employees=employees   #here we storing the value.
        
#       def empadd(self,emp):
#           if emp not in self.employees:#emp used to add new users in variable emp.
#              self.employees.append(emp)
             

#       def rmemp(self,emp): 
#           if emp in self.employees:
#              self.employees.remove(emp)

#       def printemp(self):
#           for allemp in self.employees:
#               print("Employees are ----->",allemp.fullname())



# dev1=developer('Tom','Ward',78000,'Python')  
# dev2=developer('Jinny','Mathew',88000,'Java')
# dev3=developer('Rudran','Ravi',88000,'C+')      


# mgr=manager("david",'mathew',100000,[dev1])        

# print(mgr.first)
# print(mgr.last)
# print(mgr.mail)
# print(mgr.employees)

# mgr.printemp()#here we store values of object dev1 to variable employees defaultly so we get the value of dev1 object here.
# mgr.empadd(dev2)#Here dev2 is store to emp in method(function) empadd and check condition there.here nothin will print because we not give any print condition there.
# mgr.empadd(dev3)#Here we set an argument in the method empadd and rmemp so we give value dev3.dev3 pass to emp.
# mgr.rmemp(dev1)
# mgr.printemp()



###########################################################################################################

# class parent():
#       def __init__(self,name,eyeclr):
#           self.name=name
#           self.eyeclr=eyeclr

#       def show_info(self):#here we also give the same method name in both parent class and child class.
#           print(self.name + ' eye color is '+self.eyeclr)

# class child(parent):
#       def __init__(self,name,eyeclr,no_of_toys):
#           parent.__init__(self,name,eyeclr)#here we can mention this like super method,here we need to metion the self also.          
#           self.no_of_toys=no_of_toys

#       def show_info(self):
#           print(self.name+' eye color is '+self.eyeclr+' and no. of toys are '+str(self.no_of_toys))    
    

# pa=parent('Tuco','Brown')


# pa.show_info()##here we are not calling any child class priority only to parent class.so,call the parent class method.

# ch=child('Jesse','Black',6)#here the object is child class so the values are taken from this.

# ch.show_info()##here we give the same function name in both child class and parent class here we give priority to child class so it call the function(method) in child class.


# print(isinstance(pa,parent))

# print(isinstance(ch,parent))

# print(isinstance(ch,child))


################################################################################################################

#__repr__ and __str__ method


#The repr() function returns the string representation of the value passed to eval function by default.
# For the custom class object, it returns a string enclosed in angle brackets that contains the name and address of the object by default.
# Override the __repr__() method to change this default behaviour, as shown below.

#Dunder methods are names that are preceded and succeeded by double underscores, hence the name dunder. 
#They are also called magic methods and can help override functionality for built-in functions for custom classes

#Method is called by its name, but it is associated to an object (dependent).
#A method definition always includes 'self' as its first parameter.

# class employee(): 
#         empval=1.06
#         def __init__(self,first,last,pay):#This is constructor
#                 self.first=first#This are instances
#                 self.last=last
#                 self.mail=first + '.' + last + '@gmail.com'
#                 self.pay=pay

#         def __repr__(self):
#             return f'{self.first}'  
#         def __str__(self):
#             return f'{self.first} {self.last}'      
#         def fullname(self):#regular function.
#                 return f'{self.first} {self.last}'
#         def raiseamount(self):
#             self.pay=self.pay*self.empval
        

# emp1=employee('Devin','Mathew',10000000)#the values inside the object store in the instances.

# emp2=employee('Rahul','Krishna',10000000)

# emp3=employee('Alex','Mathew',10000000)

# print(emp1)#when we print this,the value inside the __repr__method automatically print.

# print(emp1)#Here we print it the priority is for __str__method.It execute automatically.
# Both methods have same function.we commonly use __str__method it print the value to string format.           
             

#########################################################################################################################################

# import datetime

# today=datetime.date.today()
# print(str(today))#we will get the result in a more structured way.
# print(repr(today))



##########################################################################################################################################


# class employee(): 
#         empval=1.06
#         def __init__(self,first,last,pay):
#                 self.first=first
#                 self.last=last
#                 self.mail=first + '.' + last + '@gmail.com'
#                 self.pay=pay

#         def fullname(self):
#                 return f'{self.first} {self.last}'

#         def raiseamount(self):
#             self.pay=self.pay*self.empval
        
#         def __add__(self,val): #self=emp1
#         #     print(val.pay)  #Here val=emp2
#         #     print(self.pay)    
#             return self.pay + val.pay
#             #emp1.pay + emp2.pay ,this is happening here.
        
#         # def __add__(self,other):
#         #     return self.first + other #only one add dunder method will work at a time

        
# emp1=employee('Devin','Mathew',60000)        
# emp2=employee('David','Mathew',65000)        

# # print(int.__add__(1,2))#here we can addition using dunder method __add__.We also need to mention the type of the value.
# # print(str.__add__('a','b'))


# print(emp1+ emp2)#Here the first parameter emp1 is store to the argument self and emp2 store to the argument val in the __add__ method.#here we need to do addition then only the __add__ dunder method will execute.

# #there are  same dunder methods are exist that is equal to operators.

# #This is also called operator overloaded.Here we adding two int values.

# # print(emp2.pay)
# # print(emp1 + 'You are Done')


##############################################################################################################################################


# class employee(): #here no need to give the () symbol in the main class.
#         empval=1.06
#         def __init__(self,first,last,pay):
#                 self.first=first
#                 self.last=last
#                 self.mail=first + '.' + last + '@gmail.com'
#                 self.pay=pay

#         def fullname(self):
#                 return f'{self.first} {self.last}'

#         def raiseamount(self):
#             self.pay=self.pay*self
        
#         def __add__(self,val):
#             return self.first + val.last
        
#         def __len__(self):
#             return len(self.fullname())


# emp1=employee('Devin','Mathew',60000)        
# emp2=employee('David','John',65000)   

# # print(len('Athisruth'))
# # print('Athisruth'.__len__())#here we used dunder method way to find the len.

# print(len(emp1))#when we call it the dunder method __len__ will automatically call.


#####################################################################################################################################################

#Getter (@property)

# class employee(): 
#         empval=1.06
#         def __init__(self,first,last):
#                 self.first=first#this is an instance variable.
#                 self.last=last
                 
               
#         @property #if we mention @property here then we don't need to call this like a method.we can call it directly,not calling like a function.
#         #Class consider this method as its property.
#         #This also known as getter method.

#         def fullname(self):
#                 return f'{self.first} {self.last}'

#         @property

#         def mail(self):
#             return f'{self.first} {self.last}'    

        

# emp1=employee('Devin','Mathew')        
# emp2=employee('David','John')  
# emp1.first='Tom' #here we only change the value in emp1.first, that is Devin changed to Tom.To avoid error we create new method for mail.

# print(emp1.first)
# print(emp1.mail)
# print(emp1.fullname)



###########################################################################################################################################################

#Setter

# class employee(): 
#         empval=1.06
#         def __init__(self,first,last):
#                 self.first=first
#                 self.last=last

#         @property  

#         def mail(self):
#             return f'{self.first} {self.last}' 
            
#         @property 

#         def fullname(self):
#                 return f'{self.first} {self.last}'

        
#         @fullname.setter

#         def fullnamee(self,name):
#             first,last=name.split()
#             self.first=first
#             self.last=last

#         @fullname.setter

#         def full(self,name):
#             first,last=name.split()
#             self.first=first
#             self.last=last

       


# emp1=employee('Devin','Mathew')        
# emp2=employee('David','John')  #first we need to set the property.
# emp1.fullnamee='Tom Park' #here pass the value 'Tom Park' to the argument name.Then we access the method fullnamee and split 'Tom Park' and saved Tom and Park to first and last.
# emp2.full="Athisruth M"
# print(emp1.fullname)#Then we call this method fullname.when we call this property this property will execute via the method fullnamee because we set a setter to the method fullnamee.
#                 #     Here we can give same method name also for both methods.

# print(emp2.full)
########################################################################################################################################################################

#Deleter


# class employee(): 
#         empval=1.06
#         def __init__(self,first,last):
#                 self.first=first
#                 self.last=last

#         @property  

#         def mail(self):
#             return f'{self.first} {self.last}' 
            
#         @property

#         def fullname(self):
#                 return f'{self.first} {self.last}'

        
#         @fullname.setter

#         def fullnamee(self,name):
#             first,last=name.split()
#             self.first=first
#             self.last=last
        
#         @fullname.deleter 

#         def fullname1(self):
#             print('Delete the value')
#             self.first=None
#             self.last=None


# emp1=employee('Devin','Mathew')        
# emp2=employee('David','John')  
# emp1.fullnamee='Tom Park'

# print(emp1.fullname)
# print(emp1.first)
# print(emp1.last)
# del emp1.fullname1#from here the deleter is start working.here first and last set to none then the values passed to the property fullname.also print "Delete the value here"
# print(emp1.fullname)#Here print none none ,because now first and last values are stored with value none.
# print(emp2.fullname)
# del emp2.fullname1
# print(emp2.fullname)

##########################################################################################################################

# Multilevel inheritance


# class person:

#       a=10
#       b=15    
          
#       def display(self):
#           print('This is person class method') 

# class employee(person): #here the employee class have access to person class.
#       def printing(self):
#           print('This is employee class')    

#       def add(self):
#           sum=self.a + self.b #here we using person class instance of class person.
#           print(sum)        

# class programmer(employee): #here the programmer class have access to employee class.
#       def show(self):
#           print('This is programmer class')      

# class manager(programmer): #here the manager class have access to programmer class.
     
#       def mg(self):
#           print('This is manager class')                



# p1=manager()

# p1.display()
# p1.printing()
# p1.show()
# p1.mg()
# p1.add()

###############################################################################################################################

#Multiple inheritance

#a class inherited many classes at a time known as multiple inheritance.

# class landanimals:
#       def display(self):
#           print('This one is lives in land')

# class wateranimals:
#       def show(self):
#           print('This one is lives in water')      

# class frog(landanimals,wateranimals):#here two classes are inherited by class frog is called multiple inheritance.
#       pass

# f1=frog()

# f1.display()
# f1.show()


###############################################################################################################################



# class vehicle:
#       def __init__(self,name,year):
#           self.name=name
#           self.year=year
#       def disply(self):
#           print('name is',self.name,'year is',self.year) 

# class car:
#       def __init__(self,brand):
#           self.brand=brand
#       def display_new(self):
#           print('The brand name is',self.brand)


# class suv(vehicle,car):
#       def __init__(self,name,year,brand):
#           super().__init__(name, year)#we can't give 4 arguments at a time it cause error.
#           car.__init__(self,brand) #Here when we give the arguments in class suv,we should give the super method also in correct order.
#                                     #otherwise it cause error.if we directly mentioning it we don't need to consider the position.
#       def display_suv(self):
#           print('name is',self.name,'year is',self.year,'brand is',self.brand)                            



# obj=suv('SUV',2022,'Toyota')
# # obj1=vehicle('SUV',2022)
# # obj2=car('BMW')
# # obj1.disply()
# # obj2.display_new()
# obj.display_suv()




########################################################################################################

#Encapsulation

#Encapsulation is one of the fundamental concepts in object-oriented programming (OOP).
#It describes the idea of wrapping data and the methods that work on data within one unit.
#This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data.


#using this we can make a class private.


# class animal:
#       def __init__(self,name):
#           self.name=name      
      
#       def display(self):
#           print(self.name)    



# a=animal('Dog')
# a.display()#This is a public class.Because its methods can call from outside the class.

######################################################################################################################

#private method 

# class car:
#       def __init__(self):
#           self.__updatecar() #here constructor automatically execute values when we call this class.

#       def drive(self):
#           print('Driving method')  
#           self.__updatecar()

#       def __updatecar(self):#right now this class method is private.we use double underscore before a method name to make a method private.
#                             #we can access a private method only inside a class.we can't access it outside.
#           print('Updating the car')


# c1=car()
# c1.drive()

# c1.__updatecar()#this will not execute because it is a private method.

###################################################################################################################
#private class variable

# class car:
#       __maxspeed=0 #private class variabele,put 2 underscore before the class variable name.
#       __name=' '
#       def __init__(self):
#           self.__maxspeed=200
#           self.__name='BMW X1'

#       def drive(self):
#           print('Driving method')  
#           print(self.__maxspeed)
        
#       def setspeed(self,speed):
#           self.__maxspeed=speed#here we change a private class variable value  inside the class.
#           print(self.__maxspeed)    
          

     

# c1=car()
# c1.drive()
# c1.setspeed(100)
# c1.drive()

# c1.__maxspeed=100#here we can't access or modify the private class variable outside the class.
# c1.drive()       #So,no change in the values.


#############################################################################################################

#Polymorphism

#Here the parent class and child class have same method  name but not execute the parent class method.
#only execute child class method.#This is called method overriding



# class A:
#       def dis(self):
#           print('This is class a method')


# class B(A):
#       def dis(self):
#           print('This is class B method')

#       def dis_a(self):
#           print('This is the second, class B method')                  


# obj=B()
# obj.dis_a()
# obj.dis()

#######################################################################################################

# class dog:
#       def sound(self):
#           print('Bow Bow!!')


# class cat:
#       def sound(self):
#           print('Meow!!')

# def makesound(animaltype):#here we set a user defined function to call the class methods.
#     animaltype.sound()

# # def makesound(animaltype,animal):#here we set a user defined function to call the class methods.
# #     animaltype.sound()
# #     animal.sound()


# objdog=dog()
# objcat=cat()


# makesound(objdog)
# makesound(objcat)


# # makesound(objdog,objcat)


########################################################################################################

# class animal:

#       def  sound(self):
#            raise NotImplementedError('Please create a method in child class')

# class dog(animal):#if we didn't give any methods  here then raise notimplementerror in method sound will execute instead of attribute error.
# #       pass
#       def sound(self):
#           print('Bow!!Bow!!')

# class cat(animal):
#         # pass
#       def sound(self):
#           print('Meow!!')

# def makesound(animaltype):#here we set a user defined function to call the class methods.
#     animaltype.sound()


# objdog=dog()
# objcat=cat()


# makesound(objdog) 
# makesound(objcat) 

###########################################################################################################
#Itreble and Itrator



# ls=[1,2,3,4]#This is an itreble.(list,tuple,string,dict,set)

# for i in ls:#loop call the __iter__ method(it is a dunder or magic method),iter method call next method and fetch value
#     print(i)    


# print(dir(ls))

# val=iter(ls)#here we convert a Itrable to Itrator using iter method,iter method call next method and fetch value.
# print(dir(val))#here we can see the __next__ method.
# print(next(val))#iterator have the ability to store the final state(previous execution statement).
# print(dir(val))#that is why we get 2 in the second print(next(val)).
# print(next(val))
# print(next(val))
# print(next(val))
# # print(next(val))#the next method will show error after the loop end.


#Here is a list of the differences between Iterable and Iterator in Python.
#An Itrable is basically an object that any user can iterate over.
#An Iterator is also an object that helps a user in iterating over another object(that is iterable)
#We can generate an iterator when we pass the object to the iter() method.

#Iterable is an object, that one can iterate over.
#Itrable are the data that can loop.


########################################################################################################

# ls=[1,2,3,4]

# val=iter(ls)

# while True:

#      try:
#           item=next(val)
#           print(item)
  
#      except StopIteration:
#              break
            

#########################################################################################################
#Concept of range

# print(list(range(1,10)))

# class myrange():
#       def __init__(self,start,end):
#           self.value = start
#           self.end = end

#       def __iter__(self):
#           return self    

#       def __next__(self):
#           if self.value >= self.end:#The raise keyword is used to raise an exception.You can define what kind of error to raise, and the text to print to the user.
#              raise StopIteration  
#           current=self.value#old self.value=1,
#           self.value+=1#new self.value=1+1=2,this value is take in next __next__ method call.
#           return current #current value is return to the for loop num variable.(ie,1 in first step)

# nums = myrange(1,10)
# for num in nums:#when we execute the loop,first value 1 pass to num at that time __iter__ method automatically call and then __iter__ method call __next__ method automatically, then all conditions check and return the value to num.
#     print(num)  #then print(num) execute.then 
# nums = myrange(1,10)
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))





# class tuco:
#       def __init__(self,a,b):#here self.a=1 and self.b=3.
#           self.a=a
#           self.b=b

#       def __iter__(self):
#           return self

#       def __next__(self):
#           if self.a>=self.b:
#              raise StopIteration
#           c=self.a
#           self.a+=1
#           return c

# d=tuco(2,10)
# for v in d:
#     print(v)    



##########################################################################################################################################

#yield 


#Yield is a keyword in Python that is used to return from 
#a function without destroying the states of its local variable and when the function 
#is called, the execution starts from the last yield statement. 

#Any function that contains a yield keyword is termed as a generator. Hence, yield is what makes a generator.

#yield is a generator,it is also a constructor.a constructor has only a __next__ method.
#yield function has same function like return.but in return no execution will work after the return statement in the same function.

#Python generators are a simple way of creating iterators
#Simply speaking, a generator is a function that returns an object (iterator) 
#which we can iterate over (one value at a time).


# def add(a=1,b=2):
#     sum=a+b
#     return sum
#     print('Hello')   

# print(add()) 


# def add(a=1,b=2):
#     sum=a+b
#     yield sum
#     print('Hello')
#     print('hii')   

# res=add() 
# for i in res:
#     print(i)    

# res=add()
# print(next(res))
# print(next(res))
# print(next(res)) 

#####################################################################################################################################
#yield example

# def even_num():
#     a=[1,2,3,4,5,6,6,7,7,7,9,10]
#     for i in a:
#         if i%2==0:
#            yield i
#            print('heloo')
   
# a=even_num()
# for j in a:
#     print(j)          


# def add(a=1,b=2):
#     sum=a+b
#     yield sum
#     yield sum+sum
#     print('Hello2')
#     print('Hii3')   

# res=add()#here yield value sum stores to the object res then sum+sum stores to the object res,then yield convert the add() as an itreble.
# print(list(res))#yield is an iterator.here the object values is only converted to list.first print statements are executed then the values in the object executed.


# def add(a=1,b=2):
#     sum=a+b
#     yield sum
#     print('Hello')
#     print('Hii')   

# res=add()
# for i in res:
#     print(i)

# def app(o):
#     r=o+1
#     yield r
#             #here yield is converting a function to an iterable.
#             #return function only return a specific value to a function call.
   
# for j in app(5):
#     print(j)

# def takevalues():
#     yield 1
#     yield 2
#     yield 3    

# res=takevalues()
# # print(next(res))
# # print(next(res))
# # print(next(res))

# for i in res:
#     print(i)    

#########################################################################################################################



# def myrange(start):
#     current=start
#     while True:
#           yield current
#           current +=1

# myrg=myrange(1)#here myrange is an object.Here we need to use next method or for loop to fetch the value.

# print(myrg)

# for i in myrg:
#     print(i) 

# print(next(myrg)) 
# print(next(myrg))      
# print(next(myrg))      
# print(next(myrg))      

############################################################################################################################

# class myrange():
#       def __init__(self,sentence):
#           self.sentence=sentence
#           self.index=0
#           self.word=self.sentence.split()

#       def __iter__(self):
#           return self


#       def __next__(self):
#           if self.index >=len(self.word):
#              raise StopIteration
#           index=self.index
#           self.index+=1
#           return self.word[index]

# myobj=myrange('Hi I am Athisruth M Satheesh') #after object assigning the parameter,the iter method will automatically call. 
# print(next(myobj))  
# print(next(myobj))  
# print(next(myobj))  
# print(next(myobj))  
# print(next(myobj))  
# print(next(myobj))  



# for i in myobj:
#     print(i)    

##########################################################################################################################


# def app(a):
#    for i in a.split():
#         yield i
# myobj=app('Hi I am Athisruth M Satheesh')
# print(next(myobj))  
# print(next(myobj))  
# print(next(myobj))  
# print(next(myobj))  
# print(next(myobj))  
# print(next(myobj))  

# OR


# for myobj in app('Hi I am Athisruth M Satheesh'):
#     print(myobj)       


#############################################################################################################################

#normal method

#square([1,2,3,4,5])

# def square(values):
#     b=[]
#     for i in values:  
#         b.append(i*i)
#     return b   

#res=print(square([1,2,3,4,5]))
#print(res)

# print()

# def square(values):
#   for i in values:
#       print(i*i)      
      
# square([1,2,3,4,5])

# print()
# #yield method

# def square(a):
#     for i in a:
#         yield i*i  
   

# myobj=square([1,2,3,4,5])

# print(next(myobj))
# print(next(myobj))
# print(next(myobj))
# print(next(myobj))
# print(next(myobj))
# print()
# for j in square([1,2,3,4,5]):
#     print(j) 

# print()

# val=[1,2,3,4,5]
# values=[i*i for i in val]
# print(values)

# print()

# val=[1,2,3,4,5]
# values=(i*i for i in val)#values is an object here when we use a round bracket.we can iterate values from an object by for loop or next method.
# print(next(values))
# print(next(values))
# print(next(values))
# print(next(values))
# print(next(values))

#or
# for j in values:
#     print(j)




##############################################################################################################################
# import memory_profiler
# from memory_profiler import profile
# import random 
# import time


# names=['Tuco','Todd','Jesse','Walter','Gustavo']
# majors=['Python','Math','Java','CPP','r']


# @profile

# def peoplelist(peoplenum):
#     res=[]
#     for i in range(peoplenum):
#         person={
#             'id':i,
#             'name':random.choice(names),
#             'major':random.choice(majors)

#         }
#         res.append(person)
#     return res



# # def peoplelist(peoplenum):
# #     for i in peoplenum:
# #         person={
# #             'id':i,
# #             'name':random.choice(names),
# #             'major':random.choice(majors)

# #         }
# #     yield person


# if __name__=='__main__':
# #    t1=time._ClockInfo()
#    people=peoplelist(1000000)


#    t2=time._ClockInfo()
#    print(f'it took {t1-t2} min')     


##############################################################################################################

#Logging

#They can store information,
#like which user or IP accessed the application.if an error occurs,
#then they can provide more insights than a stack trace by telling you what the state
#of the program was before it arrived at the line of code where the error occured.

#it is very easy to integrate with other applications.



#Logging use instead of print statement when we are working  with large amount of data.
#Mainly to track the errors that happened in which line of code and all details of the execution.
 
#Logging levels allow us to specify exactly what we want to log by seperating these into categories
#5 standard logging levels are Debug,Info,Warning,Error and Critical.

#Debug:Detailed information,typically of interest only when diagnosing problems.

#Info:Confirmation that things are working as expected.

#Warning:An indication that something unexpected happened,or indicative of some problems in the near future(e.g.'disk space low').

#The software is still working as expected.

#Error:Due to a more serious problem,the software has not been able to perform some function.

#Critical:A serious error,indicating that the program itself may be unable to continue running.



# import logging


# def add(a,b):
#     return a+b  


# def sub(a,b):
#     return a-b      
   
# def mul(a,b):
#     return a*b      
   
# def div(a,b):
#     return a/b      
      

# num1=10
# num2=5

# add_result=add(num1,num2)
# logging.warning(f'{num1} +{num2} ={add_result}')

# sub_result=sub(num1,num2)
# logging.warning(f'{num1}-{num2} ={sub_result}')

# mul_result=mul(num1,num2)
# logging.warning(f'{num1}*{num2} ={mul_result}')

# div_result=div(num1,num2)
# logging.warning(f'{num1}/{num2} ={div_result}')


#here level warning is only by default.




# import logging

# logging.basicConfig(level=logging.DEBUG) #Debug statement is more similar to the print statement functionality.
# #it execute value similar like print statement.

# def add(a,b):
#     return a+b  


# def sub(a,b):
#     return a-b      
   
# def mul(a,b):
#     return a*b      
   
# def div(a,b):
#     return a/b      
      

# num1=10
# num2=5

# add_result=add(num1,num2)
# logging.debug(f'{num1} +{num2} ={add_result}')

# sub_result=sub(num1,num2)
# logging.debug(f'{num1}-{num2} ={sub_result}')

# mul_result=mul(num1,num2)
# logging.debug(f'{num1}*{num2} ={mul_result}')

# div_result=div(num1,num2)
# logging.debug(f'{num1}/{num2} ={div_result}')


# import logging
# logging.basicConfig(filename='filelog.log',level=logging.DEBUG)


# def add(a,b):
#     return a+b  


# def sub(a,b):
#     return a-b      
   
# def mul(a,b):
#     return a*b      
   
# def div(a,b):
#     return a/b      
      

# num1=10
# num2=5

# add_result=add(num1,num2)
# logging.debug(f'{num1} +{num2} ={add_result}')

# sub_result=sub(num1,num2)
# logging.debug(f'{num1}-{num2} ={sub_result}')

# mul_result=mul(num1,num2)
# logging.debug(f'{num1}*{num2} ={mul_result}')

# div_result=div(num1,num2)
# logging.debug(f'{num1}/{num2} ={div_result}')



# import logging
# logging.basicConfig(filename='filelog1.log',level=logging.DEBUG,\
#         format='%(asctime)s:%(levelname)s:%(message)s')
       


# def add(a,b):
#     return a+b  


# def sub(a,b):
#     return a-b      
   
# def mul(a,b):
#     return a*b      
   
# def div(a,b):
#     return a/b      
      

# num1=10
# num2=5

# add_result=add(num1,num2)
# logging.debug(f'{num1} +{num2} ={add_result}')

# sub_result=sub(num1,num2)
# logging.debug(f'{num1}-{num2} ={sub_result}')

# mul_result=mul(num1,num2)
# logging.debug(f'{num1}*{num2} ={mul_result}')

# div_result=div(num1,num2)
# logging.debug(f'{num1}/{num2} ={div_result}')



# import logging
# logging.basicConfig(filename='filelo.log',level=logging.INFO,\
#         format='%(asctime)s:%(levelname)s:%(message)s') #here we set the format of the file.

#         #%(asctime)s=execution time,509 is the millisecond here.
#         #%(levelname)s=here which level we are working(here is level INFO)
#         #%(message)s=is the details that we pass to the file.
       

# class employee:
#       def __init__(self,first,last):
#           self.first=first
#           self.last=last
#           logging.info(f'created employee {self.fullname},{self.mail}') 


#       @property
#       def mail(self):
#             return f'{self.first}.{self.last}@gmail.com'
#       @property
#       def fullname(self):
#           return f'{self.first} {self.last}'      

# emp1=employee('Devin','Mathew')            



# try:
#       num=int(input('Enter the number:'))
#       assert num%2==0               
#       print('num is even')
    
# except AssertionError:
#        print('Enter the even number')     


# try:
#       num=int(input('Enter the number:'))
#       assert num%2==0,'noooo'    #(if num=0,0/2=0,here remainder =0)
#                                            #the error condition in assert ('noooo) will not work if we are using try except.

#       print('num is even')
    
# except AssertionError:
#        print('Enter the even number')   #here is the error condition we are giving. 

