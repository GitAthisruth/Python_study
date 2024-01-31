# def start_end_decorator(func):
#     def wrapper():
#         print('Start')
#         func()
#         print('End')
#     return wrapper



# def print_name():
#     print('Alex')

# print_name = start_end_decorator(print_name)#the decorator function do the samething as this line.

# print_name()



# def start_end_decorator(func):
#     def wrapper():
#         print('Start')
#         func()
#         print('End')
#     return wrapper


# @start_end_decorator
# def print_name():
#     print('Alex')

# print_name()


# def start_end_decorator(func):
#     def wrapper(*args,**kwargs):
#         print('Start')
#         result = func(*args,**kwargs)
#         print('End')
#         return result
#     return wrapper


# @start_end_decorator
# def add5(x):
#     return x+5

# result = add5(10)
# print(result)

# import functools

# def start_end_decorator(func):
#     @functools.wraps(func)
#     def wrapper(*args,**kwargs):
#         print('Start')
#         result = func(*args,**kwargs)
#         print('End')
#         return result
#     return wrapper


# @start_end_decorator
# def add5(x):
#     return x+5

# print(help(add5))
# print(add5.__name__)



# import functools

# def start_end_decorator(func):
#     @functools.wraps(func)
#     def wrapper(*args,**kwargs):
#         print('Start')
#         result = func(*args,**kwargs)
#         print('End')
#         return result
#     return wrapper


# @start_end_decorator
# def add5(x):
#     return x+5

# # print(help(add5))
# print(add5.__name__)






import functools
from typing import Any


#nested decorators


# import functools

# def start_end_decorator(func):
#     @functools.wraps(func)
#     def wrapper(*args,**kwargs):
#         print('Start')
#         result = func(*args,**kwargs)
#         print('End')
#         return result
#     return wrapper


# def repeat(num_times):
#     def decorator_repeat(func):
#         @functools.wraps(func)
#         def wrapper(*args,**kwargs):
#             for _ in range(num_times):
#                 result = func(*args,**kwargs)
#             return result
#         return wrapper
#     return decorator_repeat

# @repeat(num_times=4)
# def greet(name):
#     print(f"Hello {name}")

# greet('Alex')


# import functools

# def start_end_decorator(func):
#     @functools.wraps(func)
#     def wrapper(*args,**kwargs):
#         print('Start')
#         result = func(*args,**kwargs)
#         print('End')
#         return result
#     return wrapper

# # second decorator

# def debug(func):
#     @functools.wraps(func)
#     def wrapper(*args,**kwargs):
#         args_repr = [repr(a) for a in args]
#         kwargs_repr = [f"{k}={v!r}" for k,v in kwargs.items()]
#         signature = ", ".join(args_repr + kwargs_repr)
#         print(f"Calling {func.__name__}({signature})")
#         result = func(*args,**kwargs)
#         print(f"{func.__name__!r} returned {result!r}")
#         return result
#     return wrapper



# @debug#second decorator
# @start_end_decorator
# def say_hello(name):
#     greeting = f'Hello {name}'
#     print(greeting)
#     return greeting


# say_hello('Athisruth')



# class CountCalls:
#     def __init__(self,func):
#         self.func = func
#         self.num_calls = 0

#     def __call__(self,*args,**kwargs):#here instance behave like a function and can call it like a function.
#         # print('Hi there')
#         self.num_calls += 1
#         print(f'This is executed {self.num_calls} times')
#         return self.func(*args,**kwargs)

# cc= CountCalls(None)#instance
# # cc()
# @CountCalls
# def say_hello():
#     print('Hello')

# say_hello()
# say_hello()











