# a = sorted(list(set(map(int,input().split()))))
# print(a)

# print(type(a))
# print(len(a))

# print(abs(4 -10))

# max_val = a[-1]
# other_val = a[:-1]
# print(max_val)
# print(other_val)

# if len(a) == 1:
#     print("Yes")
# else:
#     for i in other_val:
#             print(i)
#             if abs(max_val-i)>1:
#                 print(abs(max_val-i))
#                 print("No")
#                 break
                
#             else:
#                 print("Yes")
#                 break
                



# a = sorted(list(set(map(int,input().split()))))

# first_val = a[0]

# last_val = a[-1]

# if abs(first_val - last_val) <=1 or len(a)==1:
#         print("Yes")
# else:
#     print("No")


# ls = [3, 3, 3, 1, 2]
# ls = sorted(list(set(map(int,input()))))
# if len(ls)==1 or len(ls)==0:
#     print("Yes")
# else:
#     for i in ls[1:]:
#         print("i",i)
#         j = ls[0]
#         print("j",j)
#         if abs(j-i)>1:
#             print("No")
#             break
#         ls.pop(0)
#         if len(ls)==1:
#             print("Yes")



ls = [1,2,4]
ls = sorted(list(map(int,ls)))

flag = "Yes"
for i in range(len(ls)-1):
    if abs(ls[i]-ls[i+1])>1:
        flag = "No"
        break
    else: 
        flag = "Yes"

print(flag)


        
     
        


