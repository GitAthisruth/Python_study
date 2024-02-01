"""
- The difference between arguments and parameters
- Positional and keyword arguments
- Default arguments
- Variable-length arguments (*args and **kwargs)
- Container unpacking into function arguments
- Local vs. global arguments
- Parameter passing (by value or by reference?)

"""  


# def print_name(name):
#     print(name)


# print_name('Athisruth')


# def foo(a,b,c,d=4):
#     print(a,b,c,d)


# foo(c=1,b=2,a=3)#in keyword arguments only keyword matters not position.


# foo(1,2,3,7)#only takes default value ie,7.



# def foo(a,b, *args,**kwargs):# *args - for positional arguments, **kwargs - for keyword arguments. 
#     print(a,b)
#     for arg in args:
#         print(arg)
#     for key in kwargs:
#         print(key,kwargs[key])

# foo(1,2,3,4,5,six = 6, seven = 7)



# def foo(a,b,*,c,d):
#     print(a,b,c,d)

# foo(1,2,c=3,d=4)


# def foo(*args,c,d):
#     print(c,d)

# foo(1,2,c=3,d=4)



# def foo(*args,last):
#     for arg in args:
#         print(arg)
#     print(last)

# foo(1,2,3,last=4)



# def foo(a,b,c):
#     print(a,b,c)

# my_list = [0,1,2]#worked as a list 

# foo(*my_list)



# def foo(a,b,c):
#     print(a,b,c)

# my_tuple = (0,1,2)#worked as a tuple 

# foo(*my_tuple)


# def foo(a,b,c):
#     print(a,b,c)

# my_dict = {'a':1,'b':2,'c':3}#worked as a tuple 

# foo(**my_dict)


# local and global variables

# def foo():
#     x = number
#     print('number inside function:', x)

# number = 0
# foo()



# def nes():
#     n = name
#     print(f'my name is {n}')
# name = "Athisruth"
# nes()




# def foo():
#     x = number
#     number = 3 #this is local variable.
#     print('number inside function:', x)

# number = 0 #this act as a global variable.
# foo()




# def foo():
#     global number
#     x = number
#     number = 3 #this is local variable.
#     print('number inside function:', x)

# number = 0 #this act as a global variable.
# foo()



# def foo(x):
#     x = 5
# var = 10#global variable
# foo(var)#more priority to global variable value
# print(var)


# #appending mutable objects
# def foo(a_list):
#     a_list.append(4)

# my_list = [1,2,3]
# foo(my_list)#more priority to global variable value
# print(my_list)



# def foo(a_list):
#     a_list += [200,300,400]
#     a_list.append(4)

# my_list = [1,2,3]
# foo(my_list)#more priority to global variable value
# print(my_list)











