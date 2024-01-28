# def sum(a,b):
#     global a,b 
#     a=int(input('enter a num:'))
#     b=int(input('enter a num:'))
#     sum=a+b
#     print(sum)
# sum(a,b)

# a=int(input('Enter a:'))
# b=int(input('Enter b:'))
# c=a/b
# print('a/b=',c)
# print('a/b=%d'%c)
# t=7466
# y=8777
# print('the value is = %d and %f'%(t,y))
# u='the values are {h} and {j}'.format(h=456,j=66366)
# print(u)

# import time
# import random


# print('Printing lottery tickets.... \nPlease wait!!!')
# time.sleep(5)
# tickets=[]
# for i in range(100):
#     tickets.append(random.randrange(100000,1000000))
# print(tickets)
# winner=random.choice(tickets)
# print('The winner is...')
# time.sleep(10)
# s=f'{winner} is the winner!!!!!\n Congratulation!!!!!'
# print(s)


# str=None
# print(str==None)

############################################################################################################################################################################
# class Vehicle():
#       def __init__(self,brand,speed,mileage):
#           self.brand=brand
#           self.speed=speed
#           self.mileage=mileage

# class Bus(Vehicle):
#       def call(self):
#           return f'{self.brand} {self.speed} {self.mileage}'

# bus=Bus('Volvo','100mph','6kmh')
       
# print(bus.brand)
# print(bus.call())


# class employee():
#       def __init__(self,first,last):
#           self.first=first
#           self.last=last

#       def fullname(self):
#           return f'{self.first} {self.last}'

# class developer(employee):
#       def __init__(self, first, last,prlng):
#         #   super().__init__(first, last)
#           employee.__init__(self,first,last)
#           self.prlng=prlng

# class manager(employee):
#       def __init__(self, first, last,employees=None):
#           super().__init__(first,last)
#           if employees is None:
#              self.employees=[]
#           else:
#                self.employees=employees

#       def addemp(self,emp):
#           if emp not in self.employees:
#              self.employees.append(emp)
#       def rmemp(self,emp):
#           if emp in self.employees:
#              self.employees.remove(emp)
#       def print_emp(self):
#           for allemp in self.employees:
#               print('The employee are------->',allemp.fullname())


# dev1=developer('Tom','Alex','Python')
# dev2=developer('Jose','Thomas','Java')
# dev3=developer('Rudran','Ravi','C+')

# mgr=manager('Alexander','Jacob',[dev1])

# # mgr.print_emp()
# mgr.addemp(dev1)
# mgr.addemp(dev2)
# mgr.addemp(dev3)
# mgr.rmemp(dev3)
# mgr.print_emp()

# print(mgr.first)
# print(mgr.last)
# print(mgr.employees)


###########################################################################################

Product=[{"Id":1,
    "Subcategory":"Television",
    "Brand":"LG",
    "Features":"45 inch LED"}]     
      
    
for i in Product:
    print(i)
    print()
    for j,k in i.items():
        print(j,':',k)
    print()
    for k in i.keys():
        print(k)
    print()
    for l in i.values():
        print(l)



