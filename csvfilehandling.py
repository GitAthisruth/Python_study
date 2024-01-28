# import csv

# with open('data1.csv','r') as r:
#     r1=csv.reader(r)
#     for line in r1:
#         print(line)
     

# with open('data1.csv','r') as readdata:
#     readfile=csv.reader(readdata)
#     with open('data2.csv','w') as writedata:
#         writefile=csv.writer(writedata)
#         for line in readfile:
#             writefile.writerow(line)
     

# with open('data1.csv','r') as readdata:
#     readfile=csv.DictReader(readdata)
#     for line in readfile:
#         print(line)


# with open('data1.csv','r') as readdata:
#     readfile=csv.DictReader(readdata)
#     with open('data1dict.csv','w') as writedata:
#         filednames=['fname','lname','email']
#         writefile=csv.DictWriter(writedata,fieldnames=filednames,delimiter='/')
#         writefile.writeheader()
#         for line in readfile:
#             writefile.writerow(line)



# with open('data1.csv','r') as readdata:
#     readfile=csv.DictReader(readdata)
#     with open('data1dict1.csv','w') as writedata:
#         filednames=['fname','lname','email']
#         writefile=csv.DictWriter(writedata,fieldnames=filednames,delimiter='/')
#         #delimiter denotes the seperator between the values
#         writefile.writeheader()
#         for line in readfile:
#             del line['email']
#             writefile.writerow(line)









  
        
    