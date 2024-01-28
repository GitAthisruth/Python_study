# def g():
#     a=dict()
#     for i in range(1,21):
#         a[i]=i*i
#     print(a)
# g()

# sub=['I','you']
# ver=['Play','Love']
# obj=['Hockey','Football']

# i play hockey
# i play football
# i love hockey
# i love football
# you play hockey
# you play football
# you love hockey
# you love football
#######################
# for i in sub:
#     for j in ver:
#         for k in obj:
#             print(i,j,k)
################################
# def sortii(a):
#     b=list(set(a))
#     b.sort()
#     print(b)
# a=[12,24,35,24,88,120,155,88,120,155]
# x=sortii(a)
#####################################
# def sort(val):
#     a=[]
#     for i in val:
#         if i not in a:
#             a.append(i)
#     return a
# val=[12,988,24,35,24,88,120,155,88,120,155]
# print(sort(val)) 
############################  
# def bmi(w,h):
#     BMI=w/h**h
#     if BMI<18.5:
#         return 'You are underweight'
#     elif BMI >18.5 and BMI<24.9:
#         return 'You are healthy,Awesome!'
#     elif BMI >25 and BMI<29.9:
#         return 'You are overweight'
#     else:
#         return 'you are obese'


 
# w=int(input('Enter your weight: '))
# h=int(input('Enter your height: '))
# print(bmi(w,h))


# string='a citizen of ekm fought and won the election'
# stop_words=['in','of','a','and','the']
# 'citizen ekm fought won election'
# a=string.split()
# b=' '.join(filter(lambda x:x not in stop_words,a))
# print(b)

#or

# a='a citizen of ekm fought and won the election'
# b=['in','of','a','and','the']
# 'citizen ekm fought won election'
# c=a.split()
# r=[]
# for i in c:
#     if i not in b:
#        r.append(i)
# print(' '.join(r))


# values=[[1,2,3],[4,5,6],['a','b']]
# o/p=[1,4,'a']-using list comprehension
# print([i[0] for i in values])


# r=[]
# for i in values:
#     r.append(i[0])
# print(r)

# a=[1,2,3,4]
# b=[10,1,6]


# [11,2,7,12,3,8,13,4,9,14,5,10]

# d=[]
# for i in a:
#     for j in b:
#         d.append(i+j)
# print(d)


# d=[i+j for i in a for j in b ]
# print(d)

# a=[1,2,3,4]
# b=[1,2,3,4]
# # #o/p=[2,4,6,8]
# g=[]
# for i in range(len(a)):
#     g.append(a[i]+b[i])
# print(g)

# a=list(map(lambda x,y:x+y,a,b))
# print(a)
# a=[a[i]+b[i] for i in range(len(a))]
# print(a)
# print(range(len(a)))

# for i in range(0,3):
#     print(a[i])

######################################
# a=[i for i in range(1,11)]
# print(a)

# num=[1.2,2.3,3.4]
# print(list(map(lambda x:int(x),num)))
# num=[1.2,2.3,3.4]
# a=[int(i) for i in num]
# print(a)

# num=[1.2,2.3,3.4]
# c=[]
# for i in num:
#     c.append(int(i))
# print(c)


# [1,2]

# [1,2]
# [3,4]
# [5,6]

# n=[[1,2],[3,4],[5,6],[7,8]]

# output=[[1,3,5,7],[2,4,6,8]]

# c=[]
# for i in range(2):
#     d=[]
#     for j in n:
#         d.append(j[i])
#     c.append(d)
# print(c)

# a=[[j[i] for j in n]for i in range(2)]
# print(a)
# print([k for k in n])


# n=[[1,2,3,4],[3,4,5,6],[5,6,9,9],[7,8,8,0]]

# a=[[j[i] for j in n]for i in range(len(n[0]))]
# print(a)


# print(list(filter(lambda x:x%2==0,range(1,11))))

# print([x for x in range(1,11) if x%2==0])

# import functools

# print(functools.reduce(lambda x,y:x+y,[1,2,3,4,5,6]))
# a=[1,2,3,4]
# print(sum([1,2,3,4]))
# print(sum([x for x in [1,2,3,4]]))



# keys=['name','age']
# values=['devin',26]

# z=zip(keys,values)
# print(dict(z))
# print(dict(zip(keys,values)))

# print({key:value for key,value in zip(keys,values)})

# n=int(input('Enter a num:'))
# num=2
# for i in range(1,n+1):
#     print(num*i,end=' ')



# mylist=[10,20,30,40,50,60,70,80,90,100]

# for i in range(len(mylist)):
#     if i%2!=0:
#        print(mylist[i])
    
# a=[mylist[i] for i in range(len(mylist)) if i%2!=0]
# print(a)

# print(mylist[1:5:2])
# print(mylist[0:5])
# print(mylist[1::2])


# a=[10,20,30,40,50]


# ls=reversed(a)
# for i in ls:
#     print(i)

# ls=len(a)-1
# for i in range(ls,-1,-1):
#     print(a[i])

# a.reverse()
# print(a)
# for i in a:
#     print(i)

# b=(a[-1:-6:-1])
# print(b)
# for i in b:
#     print(i)


# b=(a[-1::-1])
# print(b)
# for i in b:
#     print(i)



# a=[12,75,80,150,180,525,50]

# for i in a:
#     if i>500:
#         break
#     elif i>150:
#         continue
#     elif i%5==0:
#         print(i)
    

# for i in a:
#     if i>500:
#         pass
#     if i>150:
#         continue
#     if i%5==0:
#         print(i)

#An elif is guaranteed not to run when the if is true
    

# for i in a:
#     if i!=525:
#         pass
#     elif i>=500:
#         pass
#     elif i%5==0:
#         print(i)
 






#o/p=['x','xx','xxx','xxxx']

# list1=[]
# for i in range(1,5):
#     list1.append('x'*i)
# print(list1)


# def call(list1):
#     return list1
# list1=[]
# for i in range(1,5):
#     list1.append('x'*i)
# print(call(list1))

# def maping(x):
#     return 'x'*x
# print(list(map(maping,[1,2,3,4,5])))##here [1,2,3,4,5] are the itrebles.





# list=['tool',23,3.4,'bar',55,'toolbar']

# def ls(l1):
#     return l1

# l1=[]
# for i in list:
#     if type(i) is str:
#         l1.append(i)

# print(ls(l1))


# def ls(l1):
#     return l1
# l1=[]
# for i in list:
#     if isinstance(i,str):
#         l1.append(i)

# print(ls(l1))


# print([item for item in list if isinstance(item,str)])

###################################################################################

# class Vehicle():
#       def __init__(self,name,max_speed,mileage):
#           self.name=name
#           self.max_speed=max_speed
#           self.mileage=mileage
#       def bus(self):
#           return f'{self.name} {self.max_speed} {self.mileage}'    

# class vehicle(Vehicle):
#       pass
     
           
# Bus=vehicle('Volvo',80,5)

# print(Bus.bus())


#OR

# class Vehicle():
#       def __init__(self,name,max_speed,mileage):
#           self.name=name
#           self.max_speed=max_speed
#           self.mileage=mileage
      

# class vehicle(Vehicle):
#       def bus(self):
#           return f'{self.name} {self.max_speed} {self.mileage}'    
     
           
# Bus=vehicle('Volvo',80,5)

# print(Bus.bus())


#OR

# class Vehicle():
#       def __init__(self,name,max_speed,mileage):
#           self.name=name
#           self.max_speed=max_speed
#           self.mileage=mileage
      

# class vehicle(Vehicle):
#      pass

# Bus=vehicle('Volvo',80,5)

# print(self.name,self.max_speed,self.mileage)

#########################################################################################################




# class Vehicle:
#       def __init__(self,name,mileage,capacity):
#           self.name=name
#           self.mileage=mileage
#           self.capacity=capacity

#       def fare(self):
#           return self.capacity*100


# class Bus(Vehicle):#inherit parent class Vehicle
#       def fare(self):
         
#           return self.capacity*100*1.1

# objbus=Bus('Volvo',6,50)#Give priority to child class

# obj1=Vehicle('Volvo',6,50)
         
# newfare=objbus.fare()

# oldfare=obj1.fare()

# print('old  fare  is',oldfare)
# print('New fare is',newfare)


#######################################################################################################################

#Total number of digit in a number
#floor division =//(it avoids the remainder)

# num=75869
# count=0
# while num>0:
#       num=num//10
#       count=count+1

# print('Total number of digit is:',count)     
      


# print(100//9) 
# 
# #################################################################################################################     


# my_list = [1,2,2,3,1,4,5,1,2,6]
# my_finallist = [i for j, i in enumerate(my_list) if i not in my_list[:j]] 
# print(list(my_finallist))



# my_list = [1,2,2,3,1,4,5,1,2,6]
# for j, i in enumerate(my_list):
#     print(j) #j print index position
    # print(i) #i print each element in my_list.

# print(my_list[:j])

# my_list = [1,2,2,6,8,9,3,1,4,5,1,2,6]

# b=[]
# for i in my_list:
#     if i not in b:
#         b.append(i)
# print(b)


# my_list = [1,2,2,6,8,9,3,1,4,5,1,2,6]

# b=[]
# a=[b.append(i) for i in my_list if i not in b ]

# print(b)


#######################################################################################################################

# import time

# # get the start time
# st = time.time()

# # main program
# # find sum to first 1 million numbers
# sum_x = 0
# for i in range(1000000):
#     sum_x += i

# # wait for 3 seconds

# print('Sum of first 1 million numbers is:', sum_x)

# # get the end time
# et = time.time()

# # get the execution time
# elapsed_time = et - st
# print('Execution time:', elapsed_time, 'seconds')

#######################################################################################################################

