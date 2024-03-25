arr = [5,4,7,8,12,45,3,6,9,2,-3,1]

matched_arr = []
for i in range(len(arr)): #O(n)T,O(1)S  - O(n^2)T
    # print(arr[i])              #O(n)T,O(1)S
    for j in range(i+1,len(arr)):#O(n)T,O(1)S
        # print(j)#T(1),T(1)
        if arr[i] + arr[j] == 10:#O(n)T,O(1)S
            matched_arr.append(arr[i])#O(n)T,O(1)S
            matched_arr.append(arr[j])#O(n)T,O(1)S
print(matched_arr)


# for i in range(len(arr)): #T(n),S(1)
#     # print(arr[i])              #T(n),S(1)
#     for j in range(i+1,len(arr)):#T(n),S(1)
#         # print(j)#T(1),T(1)
#         if arr[i] > arr[j]:
#             arr[i],arr[j] = arr[j],arr[i]

# print(arr)

