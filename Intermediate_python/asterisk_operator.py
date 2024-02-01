# result = 2 ** 4
# print(result)

# zeros = [0,1] * 10
# print(zeros)


# zeros = "AB" * 10
# print(zeros)



# def foo(a,b,*args,**kwargs):
#     print(a)
#     for arg in args:
#         for key in kwargs:
#             print(arg,key,kwargs[key])

# foo(1,2,3,4,5,six=6,seven=7)



# def foo(a,b,*,c): #'*' used to end keywords.Here c act as keyword argument.
#     print(a,b,c)

# foo(1,2,3)


# def foo(a,b,c):#unpacking keywords.
#     print(a,b,c)

# my_list = [0,1,2]
# foo(*my_list)


# def foo(a,b,c):#unpacking keywords.
#     print(a,b,c)

# my_dict = {'a':1,'b':2,'c':3}#this is like key value pair
# foo(*my_dict)#key
# foo(**my_dict)#values


# numbers = [1,2,3,4,5,6]

# *beginning,last = numbers #*beginning takes all values except last one,last takes last value.
# print(beginning)
# print(last)


# numbers = [1,2,3,4,5,6]

# beginning,*middle,secondlast,last = numbers 
# print(beginning)
# print(middle)
# print(secondlast)
# print(last)


# my_tuple = (1,2,3)
# my_list = [4,5,6]
# my_set = {7,8,9}
 

# new_list1 = [my_tuple,my_list,my_set]

# new_list2 = [*my_tuple,*my_list,*my_set]
# print(new_list1)
# print(new_list2)



# dict_a = {'a':1,'b':2}
# dict_b = {'c':3,'d':4}
# my_dict1 = {*dict_a,*dict_b}
# my_dict2 = {**dict_a,**dict_b}
# print(my_dict1)#keys only
# print(my_dict2)#key values

