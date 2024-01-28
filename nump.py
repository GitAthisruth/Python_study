
#Numpy-(Third party Library)


#NumPy, which stands for Numerical Python, is a library consisting of multidimensional array objects and a collection of routines for processing those arrays. 
# Using NumPy, mathematical and logical operations on arrays can be performed.

#NumPy is a Python package. It stands for ‘Numerical Python’.
#It is a library consisting of multidimensional array objects and a collection of routines for processing of array.
# NumPy is a Python library used for working with arrays.
#ndarray -the array object in numpy is called ndarray.

#Computer store data as binary format.

#we can store 32 or 64 bit in array.

#1 bit is 8 byte 


# stud1_maths=85
# stud1_phy=65
# stud1_bio=75
# stud1_mala=95

#Arrays

#Arrays are data structures containing a number of data values of same type.
 #Data structure is a format for organizing and storing data.
 #Also,each data structure is designed to organize data to suit a specific purpose.

#We use array instead of list because list use more memory.

#We can use list or tuple in arrays.

#In arrays data stored as a tree format.Tree format is 1D,2D,3D.

#We should give same data type in an array otherwise it throw an error(Typeerror).

#we should give same number of elements in each rows otherwise it throw error.

#A Matrix is a 2D array of numbers.

# from numpy import*

#0 dimension


# a=array(3)

# print(a)

#only one value



#1 dimension

# a=array([3])

# print(a)



# a=array([3,4,5])

# print(a)


#Only one row otherwise it throw error.



#2 Dimension

# a=array([[85,65,75,95,67],[6,5,90,67]]) ##we should give same number of elements in each rows otherwise it throw error.

# print(a)

# print(a.ndim)

# [[1,2,3,4,5],[6,7,8,9,10]]

# a=array([[85,65,75,95]])

# print(a)

# print(a.ndim)
#Combination of 1 D




#3 Dimension

# [[[1,2,3,4,5],[6,7,8,9,10]],[[1,2,3,4,5],[6,7,8,9,10]]]

# a=array([[[85,65,75,95],[1,4,5,6]],[[85,65,75,95],[1,4,5,6]]])#'[[[' count the square brackets of one side to know the dimension of the array.

# print(a)

# print(a.ndim)


#Combination of 2 D



#When we using a list we store size,Reference,Object type and Object value.

#But using when we using numby memory consumption is less compared to list.

#Numpy use Contiguous Memory Allocation.Contiguous Memory Allocation means data stored in a proper format.(SIMD-single instruction multiple data effective cache utilization)

#We can store data in different formats in numpy(32bit,64bit...).

#Numpy used for Machine Learning,Scientific computation...


# import numpy as np

# val =np.array([1,2,3,4,5])

# print(val)


# val =np.array([1,2,3,4,5],dtype='int')##we can mention the data type here.

# print(val)

# print(type(val))

# val =np.array([1,2,3,4,5],dtype='int32')##we can mention the bit size here.

# print(val)
# print(val.dtype)#here we get the dtype.

# val=np.array([[1,2,3,4,5],[6,7,8,9,10]])
# print(val)
# print()
# print(val.ndim)#here 'ndim' show dimension of the array.
 
# val=np.array([[1,2,3,4,5],[6,7,8,9,10]],ndmin=4)#We can set the dimension in 'ndmin'.
# print(val)

# print(val.shape)#here 'shape' show number  of rows and columns of the array.(2,5)-2 rows and 5 columns 

# print(val.itemsize)#It returns the size of the memory.

# # print(val.size)#It returns the number of elements in all rows.(here it is 5 elements in each rows that is total 10 elements)

# print(val.nbytes)#It returns the memory usage as bytes.

# import numpy as np

#Slicing of Arrays

# val=np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]])##Here we convert a value into a 2 dimensional array.
# print(val)
# print()
# print(val[0])
# print(val[1])
# print(val[0][3])

# print(val[1:3])#Here 3 represent the len, we take 1st index element to the 3rd element.
# print(val[0:])
# print(val[2:])
# print(val[0:4])

# print(val[0,3])#here we get 3rd index value of first element(first row).
# print(val[0,])#here we get all value of 0 index element.

# print(val[0,:])#it returns the all values of 0 index element,':' used to get full value of 0 index element.
                 # 0 means 0th row
# print(val[0,2:6])

# val=np.array([[1,2,3,4,5],[6,7,8,9,10]])

# print(val)
# # print(val[[0,3],[1,3]])##Doubt
# print()

# print(val[:,2])#here ':' access all row values then 2 take the 2nd index value of all row elements.

# import numpy as np

# val=np.array([[1,2,3,4,5,6,7,8],[9,10,11,12,13,14,15,16]])

# print(val)
# print()
# print(val[0,1:6:2])
# print(val[0,1:7:2])

# val=np.array([[1,2,3,4,5,6,7,8],[9,10,11,12,13,14,15,16]])
# print(val)
# print()

# val[0,4]=20
# print(val)


# val[:,2]=10,15 #here we  replace values to the 2nd index  position of all rows.
#               #here value 10 replace to first row and 15 to second row.
# print(val)


# val[:,2]=[45,156]
# print(val)

#':' used to access all the rows in an array.

##############################################################################

#slicing the 3 Dimension array.

# from numpy import*



# val=array([[[1,2],[3,4]],[[5,6],[7,8]]])

# print(val.ndim)

# print(val[0])

# print(val[1])

# print(val[0,0])#here 0 access 0 index row  then next 0 access the 0 index position value inside the first row.

# print(val[0,0,1])#here 0 access 0 index row  then next 0 access the 0 index position value inside the first row,1 access the 1 index value inside the 0 index position value.

# val[0]=9 #Here we update all the values inside the 0 index element of the array with 9.
# print(val)
# val[0]=[[9,9],[9,9]]#we can do it in both ways to update values(by just giving 9 or inside the list).use this method.here '[[9,9],[9,9]]' this represent 2 dimension row inside the 3 dimension array.

# print(val)

# val[0,1]=[9,9]

# print(val)

# val[0,:]=[9,9]

# print(val)


#################################################################################################

# import numpy as np


# print(np.zeros(6))#it returns 1 dimension array with 0 data values.Here 6 represents the number of columns in the 1 dimension array.

# print(np.zeros((2,3)))#here 2 represent the combination of 2 1 dimension arrays with 3 columns.We pass this inside a tuple.
                      #(note that,2 dimension array has 1 dimension array element,it has only 1 row,so we only need to represent the column number)
                             

# print(np.zeros((4,3,3)))#here 4 represent the combination of 4 2 dimension arrays with 3 rows and 3 columns. 

# print(np.ones(6))#it returns 1 dimension array with 0 data values.

# print(np.ones((2,3,2)))#here 4 represent the combination of 4 2 dimension arrays with 3 rows and 2 columns. 


# print(np.full((2,3,3),88))#full used to replace all the data to 88.

# print(np.full((5),88)

# print(np.full((4,5),22))

# -------------------------->row

# val=np.array([[1,2,3,4,5,6,7,8],[9,10,11,12,13,14,15,16]])
# print(val)

# print(np.full_like(val,7))#here values of array val replaces to 7 to get a new array. 


##################################################################################################

# import numpy as np

# print(np.random.rand(2,1))#here rand take random float values from 0-1 to create arrays.here 2 represents no. of 1 dimensional arrays in 2 dimensional array ,3 represent no. of columns.
# print(np.random.rand(2,3,4))#here  2 represents no. of 2 dimensional arrays in 3 dimensional array.3 represents no. of rows and 4 represents no. columns in the 2 dimension arrays.
                            #here float values defaultly taken between  0 and 1.

# print(np.random.randint(2,5))##this will get a value from 2-5(range 5),ie,zero dimension array.
# print(np.random.randint(2,8,size=(3,3)))#here the random integer values taken from 2,8(2-7(range(8))).
#                                         #here  3 represents no. of 1 dimensional arrays in 2 dimensional array ,3 represent no. of columns.

# print(np.random.randint(8,size=(3,3)))#here random integer values taken from 0-7.

# print(np.random.randint(8,size=(3,4,6)))#here the random integer values taken from 8(0-7(range(8))).
                                        #here  3 represents no. of 2 dimensional arrays in 3 dimensional array.4 represents no. of rows and 6 represents no. columns in the 2 dimension arrays.

# print(np.identity(4))##Identity matrix = it is a square matrix(same rows and columns) with diagonal elements are 1 and other elements are 0.

# val=np.array([[[1,2,3,4,5]]])

# # print(val)

# # print()

# print(np.repeat(val,3,axis=0))#here 3 means the 3 dimension array contains the  combination of 3 2 dimension array.here we set 'axis=0' so,each 2 dimension array takes the exact row of array 'val'.

# a=np.repeat(val,3,axis=0)
# print(a.shape)

# print(np.repeat(val,3,axis=1))#here we set 'axis =1'.so the 3 dimension array contains the  combination of 1 2 dimension array with 3 column of the same row of array 'val'.

# b=np.repeat(val,3,axis=1)
# print(b.shape)
# c=np.array([[[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]])

#if axis = 0 it is based on row,if axis = 1 it is based on column.          

# val=np.array([[[1,2,3,4,5]],[[1,2,3,4,5]]])

# print(np.repeat(val,3,axis=0))#here total 2rows *3 = 6 rows take.
# print()

# d=np.repeat(val,3,axis=0)

# val1=np.repeat(val,3,axis=1)
# print()
# f=np.repeat(val1,3,axis=0)
# print(f.shape)

# print(np.repeat(val,3,axis=1))#here total 2  2 dimension arrays ,each arrays with 3 2 dimension arrays.

# d=np.repeat(val,3,axis=1)
# print(d.shape)


# val=np.array([1,2,3,4,5])#1 dimension array

# print(np.repeat(val,4,axis=0))
# print(np.repeat(val,4,axis=1))#This won't work because 1 dimension array only have one row.

# val=np.array([[1,2,3,4,5],[1,2,3,4,5]])#2 dimension array

# print(np.repeat(val,4,axis=0)) #same like 3 dimension array.4*2(total number of combination of 1 dimension array)
# print(np.repeat(val,4,axis=1))#Combination of 2 1 dimension arrays with 4 * 5(length of one row value).total 2 rows.


#######################################################################################################

# [[1. 1. 1. 1. 1.]
#  [1. 0. 0. 0. 1.]
#  [1. 0. 9. 0. 1.]
#  [1. 0. 0. 0. 1.]
#  [1. 1. 1. 1. 1.]]

# import numpy as np

# val=np.ones((5,5))
# val[1:4,1:4]=0
# print(val)
# val[2,2]=9
# print(val)
# print(np.ndim(val))





# val=np.ones((5,5))


# val[1:4,1:4]=0

# print(val)


# val[2,2] = 9

# print(val)

#OR

# one =np.ones((5,5))

# print(one)

# ze = np.zeros((3,3))

# print(ze)

# ze[1,1]=9
# print(ze)
# one[1:-1,1:-1] =ze

# print(one)

###################################################################################

# import numpy as np

# arr =np.array([1,2,3,4])

# print(arr)

# a=arr
# print(a)
# a[1]=10#1 dimension array always has 1 row so here 1 represent 1th index position value of the row.
# print(a)
# print(arr)

# a=arr.copy()#here we create a copy of main file  to avoid the changes that happen to main file.

# # print(a)
# a[1]=10
# print(arr)
# print(a)


###################################################################################################

#Mathematical operations in an Array




# import numpy as np



# a = np.array([1,2,3,4])

# print(a)

# print()

# print(a+2)
# print(a-2)
# print(a*2)
# print(a**2)

# a = np.array([1,2,3,4])
# b = np.array([5,6,7,8])

# print(a+b)
# print(np.sin(a))
# print(np.cos(a))
# print(np.tan(a))#tan=sin/cos


####################################################################################

# import numpy as np

# a=np.ones((2,3))

# print(a)

# print()

# b=np.full((3,2),2)
# print(b)
# print()

# print(np.matmul(a,b))#This is matrix multiplication, that is  (Row of first matrix) * (column of second matrix)
                    #add values as row base.

# val=np.array([[1,2,3],[1,1,1]])

# print(val)

# print()

# val1=np.array([[1,2],[1,1],[1,1]])

# print(val1)

# print()

# print(np.matmul(val,val1))

#How to find a determinant.

# arr=np.identity(3)

# print(arr)
# print()
# print(np.linalg.det(arr))#'linalg'-linear algebra.'det' is the determinant.

# arr=[[1. 0. 0.]
#      [0. 1. 0.]
#      [0. 0. 1.]]


# det(arr) or |arr|= 1(1*1-0*0)-0(0*1-0*0)+0(0*0-0*1)#this is how  to find a determinant of a matrix


############################################################################################

# import numpy as np

# val=np.array([[1,2,3],[1,1,1]])

# print(val)

# print(np.min(val))

# print(np.max(val))

# print(np.mean(val))#The mean is the average where the sum of all the numbers is divided by the total number of numbers.
#                    #9/6=1.5

# print(np.median(val))#the median is the middle value in the list of given numbers numerically ordered from smallest to biggest 
                     #1,1,1,1,2,3( For an even set of numbers Median = ( (n/2)th observation+(n/2 +1)th observation ) / 2.)ie,(1+1)/2=1





# import numpy as np



#Reshape

#here we should reshape based on the total elements of the original array.

# val=np.array([[1,2,3,4],[5,6,7,8]])

# print(val)

# print(val.shape)

# before=np.array([[1,2,3,4],[5,6,7,8]])

# print(before)

# print()

# after =before.reshape(4,2)

# print(after)

# print()

# after =before.reshape(2,2,2)
# after =before.reshape(1,2,2)#this will throw error because all values can't fill in the given array.

# print(after)


###############################################################################################


#Stacking

#stack means arrangement,we can stack any number of arrays.

# import numpy as npt


# a=np.array([1,2,3,4])

# print(a)

# print()

# b=np.array([5,6,7,8])
# c=np.array([8])
# print(b)
# print()
# print(np.vstack([a,b]))#it gives given arrays as rows ,now it is 1 dimension but we can give any dimension by increasing the square brackets.

# print(np.vstack([a,b,c]))#throw error ,c has not same number of rows
# print()
# print(np.hstack([a,b]))#it gives arrays as columns
# print(np.hstack([a,b,c]))#it cause no error ,columns is only considering here.so, row of c not a problem.


#############################################################################################

# import numpy as np

# print(np.arange(5))#This is array range,we can set range here,here we get a 1 dimension array.

# print(np.arange(5,12))#range 5-11

# print(np.arange(1,12,2))#range 1-11,2 is the common difference.

# print(np.arange(12).reshape(3,4))#Check given range is equal  to the total array values.

# print(np.linspace(1,2,9))#here take float values  between 1 and 2, 1,2 also include here.9 denotes the length of the array.#This is also 1 dimension array.

# val=np.array([[1,2,3,4],[5,6,7,8]])

# print(val.ndim)

# print(val.shape)
# print(np.shape(val))


# print(val.ndim)

# new=val.ravel()#ravel function convert an array above 1 dimension to 1 dimension array.

# print(new)

# print(new.ndim)

# val=np.array([[[1,2,3,4],[5,6,7,8]]])
# print(val)
# print(val.shape)

# new=val.ravel()
# print(new)

# print(new.ndim)


###########################################################################################