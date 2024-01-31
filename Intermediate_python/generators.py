#generators are functions that returns an iterator using the Yield keyword.

#very memory efficient in large values.


# def mygenerator():
#     yield 1
#     yield 2
#     yield 3

# g = mygenerator()

# print(list(g))

# for i in g:
#     print(i)

# value = next(g)#return first value
# print(value)
# value = next(g)#return second value
# print(value)


# def mygenerator():
#     yield 1
#     yield 2
#     yield 3

# g = mygenerator()

# print(sum(g))
# print(sorted(g))


# def countdown(num):
#     print('Starting')
#     while num > 0:
#         yield num
#         num -= 1

# cd = countdown(4)

# value = next(cd)
# print(value)
# print(next(cd))
# print(next(cd))
# print(next(cd))
# print(next(cd))

#great advantage of a generators is to fetch the first value from an iterator without iterating it fully. 

# n=6
# while n >0:
#     n-=1
#     print(n)


# import sys

# def firstn(n):
#     nums = []
#     num = 0
#     while num < n:
#         nums.append(num)
#         num += 1
#     return nums

# # generator

# def first_generator(n):
#     num = 0
#     while num < n:
#         yield num
#         num += 1

# mylist = firstn(10)

# print(mylist)

# print(sum(firstn(10000)),"size is :",sys.getsizeof(firstn(10000)))

# print(sum(first_generator(10000)),"size is :",sys.getsizeof(first_generator(10000)))

# print(sys.getsizeof(firstn(10000000)))
# print(sys.getsizeof(first_generator(10000000)))


# def fibonacci(limit):
#     #0 1 1 2 3 5 8 13 ...
#     a,b = 0,1
#     while a < limit:
#         yield a 
#         a,b = b,a+b

# fib = fibonacci(3)
# for i in fib:
#     print(i)



# generator expression

# import sys

# mygenerator = (i for i in range(100000) if i % 2 == 0)
# print(next(mygenerator))
# print(next(mygenerator))
# next(mygenerator)
# print(list(mygenerator))
# print(sys.getsizeof(mygenerator))
# for i in mygenerator:
#     print(i)

#list comprehension
    
# mylist = [i for i in range(100000) if i % 2 == 0]
# print(mylist)
# print(sys.getsizeof(mylist))

# for i in mylist:
#     print(i)








