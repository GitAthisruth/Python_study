

# # # from asyncore import file_dispatcher
# # # from venv import create


# # # x is for creating new file
# # # r for read a file
# # # w for  write a file
# # # a for append the new values to the file_dispatcher
# # # br is for binary read for read the image files




# # # 1.open a file
# # # 2.operations
# # # 3.close the file

# # # f=open("sample.csv",'x')
# # # print(f)

# # # 
# # # f=open("sample.txt",'w')
# # # f.write("line number 1\n")
# # # f.write("line numbver2\n")
# # # f.write("line number 3\n")
# # # f.close()


# # # f=open("sample.txt",'r')
# # # new=f.read()
# # # print(new)
# # # f.close()

# # # f=open("sample.txt",'r')
# # # new=f.readline()
# # # print(new)
# # # f.close()


# # # a=open("abin.py","x")
# # # a=open("abin.py","w")
# # # a.write("c=5+6\n")
# # # a.write("print(c)")
# # # a.close

# # # a=open("abin.py","r")
# # # n=a.readline()
# # # v=a.readline()
# # # print(n)
# # # print(v)
# # # a.close()

# # # f=open("sample.txt",'r')
# # # new=f.readlines() 
# # # for i in new:    ##for fetching all the lines in the file
# # #     print(i)
# # # f.close()

# # # f=open("sample.txt",'r') 
# # # new=f.readlines()
# # # print(new[2])    ####for fetching a particular line using index position of line
# # # f.close()

# # # f=open("sample.txt","w")
# # # f.write('abin')
# # # f.close()

# # # f=open("sample.txt","a") ###to append a new line without overwriting
# # # f.write('abin')
# # # f.close()


# # # f=open("sample.txt","br")
# # # new=f.read()
# # # print(new)
# # # f.close()

# # # f=open("sample.txt","a")
# # # f.write('The new value added')
# # # new=f.read()
# # # print(new)
# # # f.close()

# # # f=open("sample.txt","r")
# # # print(f.tell()) ##tell function will tell where the cursor's position after the execution 
# # # new=f.readline()
# # # print(new[0])
# # # print(f.tell())
# # # print(f.readline())
# # # print(f.tell())

# # f=open('sample.txt',"r")
# # print(f.tell())
# # new=f.readline()
# # print(new[0])
# # print(f.tell())
# # print(f.readline())
# # print(f.tell())
# # f.seek(2) ### cursor will be placed back two the second position 
# #           ### we can specify the position inside the seek where want to 
# #           #3replace the cursor position
# # print(f.tell())
# # print(f.readline()) ##  now  it will read from the position where cursed is placed

# # with open("sample.txt",'r') as f: #we don't have to close the file manually
# #     f=f.read() 
# #     print(f)

# f=open('sample.txt','r+')  #r+ means read and write
#                            # w+ can be used for write and read
# new=f.read()
# print(new)

# f=open("sample.txt","a")
# f.write("newtwo line number 2\n")

# f=open("sample.txt","w")
# f.write("nwtwo line nunmber 2\n")

# f=open('sample.txt','r')
# new=f.read()
# print(new)

# 

# with open("sample.txt",'r') as f:
#     for line in f:
#         print(line)
    
# import os
# # os.remove("sample.txt")    

# print(dir(os))


# import pandas
# print(dir(pandas))  #we can find all the sub modules in a module using dir functions


# f=open('sample.csv',"w")
# f.write("line one\n")
# f.write('line two\n')


# f=open("sample.csv","r")
# new=f.read()
# print(new)

# import pandas as pd
# f=pd.read_csv("sample.csv")  #read csv is a inbuilt function in pandas module
# print(f)

# import os
# os.remove("sample.csv") #to remove a file


text_to_search = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa .077
MetaCharacters (need to be escaped):
. ^ $ * + ? { } [ ] \ / ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
900-555-1234
Mr. Schafer
Mr Smith
ms Davis
Mrs. Robinson
Mr. T
'''


import re

pattern=re.compile(r'\d{3}.\d{3}.\d{4}')
with open('C:/Users/athis/Downloads/data1.txt') as file:
     content=file.read()
     matches=pattern.finditer(content)
for match in matches:
    print(match)

with open('sample3.txt','w') as new:
     new.write(content)
