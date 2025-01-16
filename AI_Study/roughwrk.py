# sample_list = [1,2,3,4,5]

# def fc(ls):
#     ls = map(lambda x:x+1,ls) 
#     return ls


# print(list(fc(sample_list)))
# print(sample_list)


# sample_list = [1,2,3,4,5]

# print(sample_list.pop())

#Stack 

#1.Stack add elements from bottom to top.
#2.If we want to delete or insert an element in the middle or bottom part of a stack we need to pop the top elements first to another stack and insert or delete the respected element and then append the safe stack.

# words = input("Give four words: ")
# safe = []
# if words:
#     stack = words.split()
#     print(f"Our stack {stack}")
#     stack_len = len(stack)
#     print(stack_len)
#     while stack_len > 0:
#         pop_operation = stack.pop()
#         print(f"started to pop top elements from the stack {pop_operation} ")
#         stack_len -= 1
#         safe.append(pop_operation)
#         print(f"safe {safe}")
#         print(f"safe pop {pop_operation}")
#     len_ = len(safe)
#     while len_ > 0:
#         len_ -= 1
#         deleted = safe.pop()
#         if len(deleted) > 10:
#                 print(f"element greater than 10 {deleted} and {len(deleted)}")
#                 new_word = str(deleted[0]) + str(len(deleted) - 2) + str(deleted[-1])
#                 stack.append(new_word)
# else:
#     print("Add any words..")


# print(f"The words in stack are {stack}")

# print(safe)     
    


# wordsss = ['adsjkljhdsj','kdfkhjkdskjhads','zahklsdhsk','dsghghjdsdjha']

# deleted = wordsss.pop()


# print(str(deleted[0]) + str(len(deleted)-2) + str(deleted[-1]))


      
# converting the words

# stack=[]
# safe = ['dakhjjkdsaklhadskhljhjkads', 'jkdsajkhjbdashgjhjads'] 

# print(stack)

        


# words = input("Give four words: ")
# safe = []
# if words:
#     stack = words.split()
#     print(f"Our stack {stack}")
#     stack_len = len(stack)
#     print(stack_len)
#     while stack_len > 0:
#         pop_operation = stack.pop()
#         print(f"started to pop top elements from the stack {pop_operation} ")
#         stack_len -= 1
#         safe.append(pop_operation)
#         print(f"safe {safe}")
#         print(f"safe pop {pop_operation}")
#         safe_pop = safe.pop()
#         if len(safe_pop) > 10:
#                 print(f"element greater than 10 {safe_pop} and {len(safe_pop)}")
#                 new_word = str(safe_pop[0]) + str(len(safe_pop) - 2) + str(safe_pop[-1])
#                 stack.append(new_word)
# else:
#     print("Add any words..")
    
# print(f"The words in stack are {stack}")


val = input("enter a val between 0 and 151 first and add statements 'X++ for addition and --X for substraction only': ")

val = val.strip().split()
# print(val)
# print("val",val[1:])
X = 0
# print(X)

for i in val:
        # print(i)
        if i in ["X++","++X"]:
            X += 1
        elif i in ["--X","X--"]:
            X -= 1
print(f"final value of X is: {X}")
    

    

    
    

