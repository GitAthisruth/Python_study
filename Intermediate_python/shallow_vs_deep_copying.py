# - shallow copy: one level deep, only references of nested child objects.
# - deep copy: full independent copy.


#In mutable types not work like this way.
# org = 5
# cpy = org
# cpy = 6

# print(cpy)
# print(org)



# org = [0,1,2,3,4]
# cpy = org#here we can see both original and dyplicate are changed.
# cpy[0] = 10

# print(cpy)
# print(org)


#shallow_copy - only one level deep.

# import copy

# org = [0,1,2,3,4]
# # cpy = copy.copy(org)
# cpy = org.copy()
# cpy[0] = 10

# print(org)
# print(cpy)



# import copy

# org = [0,1,2,3,4]
# # cpy = copy.copy(org)
# cpy = list(org)
# cpy[0] = 10

# print(org)
# print(cpy)


# import copy

# org = [0,1,2,3,4]
# # cpy = copy.copy(org)
# cpy = org[:]
# cpy[0] = 10

# print(org)
# print(cpy)




# import copy 

# org = [[0,1,2,3,4],[5,6,7,8,9]]
# cpy = copy.copy(org)#here we can see both original and duplicate are changed in shallow copy of nested list,arrays etc. 
# # cpy = org[:]
# cpy[0][0] = 10

# print(org)
# print(cpy)





# Deep copy



# import copy 

# org = [[0,1,2,3,4],[5,6,7,8,9]]
# cpy = copy.deepcopy(org)
# cpy[0][0] = 10
# print(org)
# print(cpy)



# import copy 

# org = {'w':{'a':2,'b':6}}#doing copy for two levels we must use deep copying method.
# cpy = copy.copy(org)
# cpy['w']['a'] = 10
# print(org)
# print(cpy)



# import copy 

# org = {'w':{'a':2,'b':6}}#doing copy for two levels we must use deep copying method.
# cpy = copy.deepcopy(org)
# cpy['w']['a'] = 10
# print(org)
# print(cpy)



# import copy

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# p1 = Person('Alex',23)#object
# p2 = copy.copy(p1)#shallow copy of the object

# p2.age = 34

# print(p2.age)
# print(p1.age)




# import copy

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# class Company:
#     def __init__(self,boss,employee):
#         self.boss = boss
#         self.employee = employee     

# p1 = Person('Alex',23)#object
# p2 = Person('Joe',17)#object
# # p2 = copy.copy(p1)#shallow copy of the object-copy of the reference only.

# company = Company(p1,p2)
# company_clone = copy.deepcopy(company)
# company_clone.boss.age =56
# print(company_clone.boss.age)
# print(company.boss.age)




