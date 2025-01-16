# #Important stacks

# stack = []
# safe = []

# # Important functions

# def insert(stack,element):
#     stack.append(element)
#     print(stack)
# def pop(stack):
#     stack.pop()
# def length(stack):
#     return len(stack)
# def top(stack):
#     return stack[-1]
# def display_stack(stack):
#     return stack
# def delete(stack,safe,element):
#     while top(stack) != element and length(stack) != 0:
#         safe.append(stack.pop())
#         print(f"stack:{display_stack(stack)} and safe:{safe}")
#     if length(stack) != 0:
#         pop(stack)
    
#     while len(safe)!=0:
#         insert(stack,safe.pop())
#     print(f"stack after deletion is:{stack}")

# def insert_at_index(stack,safe,target_index,element):
#     target_iter = length(stack)-target_index
#     print(target_index)
#     while  target_iter > 0:
#         safe.append(stack.pop())
#         print(f"stack{stack} safe {safe}")
#         target_iter-=1

#     stack.append(element)
#     while len(safe)!=0:
#         insert(stack,safe.pop())
#     print(f"Original stack after insertion at Index {target_index}: {stack}")

        
# insert(stack,5)
# insert(stack,8)
# insert(stack,20)
# insert(stack,35)
# insert(stack,12)
    
# print(top(stack))

# # delete(stack,safe,20)
# insert_at_index(stack,safe,4,100)
# print(stack)

# import torch
# print(torch.cuda.is_available())

# print(torch.__version__)

# list = [2,3,4,5,6,99,11,3,6,88,5,3,1,7]

# val = list[0] 
# for i in list:
#     if i < val:
#         val = i
# print(f"lowest value is {val}")

