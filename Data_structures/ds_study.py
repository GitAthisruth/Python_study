# arr = [5,4,7,8,12,45,3,6,9,2,-3,1]

# matched_arr = []
# for i in range(len(arr)): #O(n)T,O(1)S  - O(n^2)T
#     # print(arr[i])              #O(n)T,O(1)S
#     for j in range(i+1,len(arr)):#O(n)T,O(1)S
#         # print(j)#T(1),T(1)
#         if arr[i] + arr[j] == 10:#O(n)T,O(1)S
#             matched_arr.append(arr[i])#O(n)T,O(n)S
#             matched_arr.append(arr[j])#O(n)T,O(n)S
# print(matched_arr)


# for i in range(len(arr)): #T(n),S(1)
#     # print(arr[i])              #T(n),S(1)
#     for j in range(i+1,len(arr)):#T(n),S(1)
#         # print(j)#T(1),T(1)
#         if arr[i] > arr[j]:
#             arr[i],arr[j] = arr[j],arr[i]

# print(arr)





# spell = "abracadabra"
# frequency = {}
# for i in spell:
#     print(i)
#     if i in frequency:#This line checks if the current character i already exists as a key in the frequency dictionary.
#         frequency[i] += 1
#     else:
#         frequency[i] = 1
# print(frequency)



# arr1 = [6,4,6,8,6,12,6,3,5,9,2,-3,1,8,4,6]
# print("len of arr1 is",len(arr1))
# n = len(arr1)/2
# # print(round(n))
# if isinstance(n,float) == True:
#     n = int(abs(n))
#     for i in range(n):
#         # print(i,rev_index)
#         rev_index = len(arr1)-(i+1)
#         if arr1[i] == 6 and arr1[rev_index] != 6:
#             arr1[i],arr1[rev_index] = arr1[rev_index],arr1[i]
#     print(arr1) 
#     for i in range(n):
#         # print(i)
#         print(len(arr1)-(i+3),arr1[len(arr1)-(i+3)])
#         # if arr1[len(arr1)-(i+1)] != 6:
#             # print("index",len(arr1)-(i+1),arr1[len(arr1)-(i+1)])
#         arr1[len(arr1)-(i+2)],arr1[len(arr1)-(i+3)] = arr1[len(arr1)-(i+3)],arr1[len(arr1)-(i+2)]
        
#         print(arr1)




    # # print(rev_index-1,rev_index)
    # # print(arr1[len(arr1)-(i+2)],arr1[len(arr1)-(i+1)])
    # if arr1[len(arr1)-(i+2)] == 6 and arr1[rev_index] != 6:
    #     arr1[rev_index-(i+1)],arr1[rev_index] = arr1[rev_index],arr1[len(arr1)-(i+1)]
       
        
    # print(arr1)
    # for i in range(len(arr1)):
    #     rev_index = len(arr1)-(i+1)
    #     print(rev_index-1,rev_index)

    
            
            # if arr1[rev_index] == 6:
            #     print(f"first {n} values {arr1[rev_index]} with index {rev_index}")
# else:
#     for i in range(n):
#         rev_index = len(arr1)-(i+1)
#         print(i,rev_index)
#         if arr1[i] == 6:
#             print(f"first {n} index values {arr1[i]} with index {i}")
#         if arr1[rev_index] == 6:
#             print(f"first {n} values {arr1[rev_index]} with index {rev_index}")



            # print(i)
            # if arr1[len(arr1)-i] != 6:
                # print(i)

            #     print(arr1[len(arr1)-i])
#                  arr1[i],arr1[len(arr1)-i] = arr1[len(arr1)-i],arr1[i]
# print(arr1)

# 1. findlength  the length of the array.
# 2. divide the array in half .
# 3. if length of the array is even then divide it and not round the num.
# 4. if the length of the array is odd then split the length to half then we get a float value.
# 5. Then round the float value.
# 6. Then check there is any value 6 in the first 6 index positions.
# 7. if yes then just swap the values with the corresponding 
# 8. if the last positions are not fully filled with 6.
# 9. Then filled the adjacent position. 


# public class sample {

#     public static int[] moveElementToEnd(int[] array,int target) {
#         int i = 0, i = array.length - 1;
#         while (i<i) {
#             while (i < i &&[i] == target) {
#                 i--;
#             }
#              if (array[i] == target)
#              int temp = array[i];
#              array[i] = array[i];
#              array[i] = temp;
#              }
#              i++;
#     }
#     return array:
# }
        

# def moveElementToEnd(array, target):
#     i = 0
#     j = len(array) - 1
#     while i < j:
#         while i < j and array[j] == target:
#             j -= 1
#         if array[i] == target:
#             array[i],array[j] = array[j],array[i]
#             # temp = array[i]
#             # array[i] = array[j]
#             # array[j] = temp
#         i += 1
#         print(array)
#     return array

# # Example usage
# array = [6, 6, 2, 4,7,6,0,6, 2, 3, 4, 6]
# target = 6
# print(moveElementToEnd(array, target))



