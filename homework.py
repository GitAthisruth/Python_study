#number of multiples

# def call(n,u):
#     count=0
#     for i in range(n):
#         if i%u==0:
#            count+=1
#     return  u,'divide',n,count,'times'
# n=int(input('Enter a num:'))
# u=int(input('Enter the diviser:'))
# print(call(n,u))

#prime number

# n=int(input('Enter a num:'))
# if n>1:
#     for i in range(2,n):
#         if n%i==0:
#            print(n,'is not a prime number')
#         break
#     else:
#         print(n,'is a prime')
# else:
#     print(n,'is not a prime')


#Vowels
######################
# n=input('Enter a string:')
# b="AEIOUaeiou"
# count=0
# for i in n:
#     for j in b:
#         if i==j:
#             count+=1
        
# print('No of vowels in',n,'is',count)

#number of digits

# n=int(input('Enter a num:'))
# count=0
# while n>0:
#     n=n//10
#     count+=1
# print('Total number of digits',count)

#count a digit in a list

# a=[1,2,3,4,5,6,4,4,56,66,56,8,3,2,9,2,5,5,5,5,9,6]
# n=int(input('Enter a num:'))
# count=0
# for i in a:
#     if i==n:
#         count+=1
# print('The No. of',n,'in the list is',count)

#counting prime numbers


# l=[]
# n=int(input('Enter a number:'))
# for j in range(2,n):
#     a=0
    # for i in range(2,j):
    #     if j%i==0:
    #         a=1
    #         break
#     if a==0:
#         l.append(j)
# print(l)






# n=int(input('Enter a number:'))
# if n:
#     print()
# for i in range(2,n):
#         if j%i==0:
#             a=1
#             break