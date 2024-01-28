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




#class in manual way

# class employee():
#     pass
# emp1=employee()
# emp1.first='Tuco'
# emp1.last='Salamanga'
# emp1.mail='tuco@gmail.com'
# emp1.pay=50000

# emp2=employee()
# emp2.first='Jesse'
# emp2.last='Pinkman'
# emp2.mail='Pinkman@gmail.com'
# emp2.pay=10000000

# print(emp1.first)
# print(emp2.first)


#class created in an automated way

# class employee():  #method is actually a function.when we use a function inside a class is called method.
#     def __init__(self,first,last,pay):
#         self.first=first
#         self.last=last
#         self.mail=first+'.'+last+'@company.com'
#         self.pay=pay



# class employee(): #Here we created a magic/dunder method
#     def __init__(hello,first,last,pay):#__init__ is  initialization.
#         hello.first=first
#         hello.last=last
#         hello.mail=first+'.'+last+'@company.com'
#         hello.pay=pay

# emp1=employee('Devin','Mathew',10000000)
# emp2=employee('Rahul','Krishna',5000000)
# emp3=employee('Alex','Mathew',10000000)

# print(emp1.first)
# print(emp1.last)
# print(emp1.mail)
# print(emp1.pay)
# print()

# print(emp2.first)
# print(emp2.last)
# print(emp2.mail)
# print(emp2.pay)
# print()

# print(emp3.first)
# print(emp3.last)
# print(emp3.mail)
# print(emp3.pay)
# print()

# print(emp1.first,emp1.last,emp1.mail,emp1.pay)
# print()


# class sample():
#     def __init__(self):#self is used to mention it is in class.Here we always use self it is a standard name.
#         print("Hello Devin")
#     def me(self):
#         print("Hi Devin")

# samp1=sample()#here we create an object,here we call the class ,it automatically call the method __init__ ,because here we use dunder method.
#method=a function inside a class
# print(samp1)
# samp1.me()#Here we need to call function seperately.Here samp1 is the object.


#A class initialization block is a block of statements preceded by 
#the static keyword that's introduced into the class's body. 
#When the class loads, these statements are executed.

# class employee():
#       def __init__(self,first,last,pay):#__init__ is  initialization.
#           self.first=first
#           self.last=last
#           self.mail=first+'.'+last+'@company.com'
#           self.pay=pay
#       def fullname(self):
#           return '{} {}\n{}\n{}'.format(self.first,self.last,self.mail,self.pay)   
#         # print('{} {}\n{}\n{}'.format(self.first,self.last,self.mail,self.pay))  
# emp1=employee('Devin','Mathew',10000000)
# emp2=employee('Rahul','Krishna',5000000)
# emp3=employee('Alex','Mathew',10000000)

# print()
# print('{} {}'.format(emp1.first,emp1.last))
# print()
# print(emp1.fullname())
# print()
# print(emp2.fullname())
# print()
# print(emp3.fullname())
# print()

# emp1.fullname()