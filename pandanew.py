#Pandas


#Pandas is an open-source library that allows you to perform data manipulation and analysis in Python.
#Pandas Python library offers data manipulation and data operations for numerical tables and time series.
# Pandas provide an easy way to create, manipulate, and wrangle the data.
# It has functions for analyzing, cleaning, exploring, and manipulating data.


#Data structures in Pandas are:
 

 #1.Series 


 #2.DataFrame


#3.Panel


#We are mostly using Series and Dataframe .


                        
#1.Series- It is a one dimensional array.

#Pandas Series is a one-dimensional labeled array capable of holding data of any type (integer, string, float, python objects, etc.).
# The axis labels are collectively called index. Pandas Series is nothing but a column in an excel sheet. Labels need not be unique but must be a hashable type.



# import pandas as pd

#pd.series(data,index,dtype,copy)##if we give copy=True we get an another copy of the data.

# print(pd.__version__)

# s=pd.Series()#Here we get an empty series.

# print(s)


# s=pd.Series(dtype='float64')

# print(s)

# import pandas as pd

# import numpy as np

# data = np.array(['a','b','c','d'])

# a=pd.Series(data)#Output is in a table format 

# print(a)
# print()

# import pandas as pd

# import numpy as np

# data = np.array(['a','b','c','d'])#if we didn't give the index postion seperately,then index value print automatically.

# a=pd.Series(data,index=[101,102,103,104])#Here we can change index position in the parameter index.

# print(a)


# import pandas as pd

# import numpy as np


# data={'a':0,'b':1,'c':2}#In the dictionary the default index is the key (Row index),each key is a row.
# a=pd.Series(data)
# print(a)
# a=pd.Series(data,index=['a','b','c'])#here index = column labels.
# print(a)
# a=pd.Series(data,index=['a','t','c','l'])#here we should use the same index value(key) in the given  dictionary.if we use other values it will print NaN(Not a Number) value to the key.
# print(a)


# import pandas as pd 

# import numpy as np

# a=pd.Series(5,index=['a','t','c','l'])#here all values print as 5.

# print(a)

# a=pd.Series(5,index=[1,2,3])

# print(a)

  

# Slicing of series

# We slice data using ':'(colon).


# import pandas as pd

# import numpy as np



# a=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])

# print(a)

# print()

# print(a[0])

# print(a[-1])

# print()

# print(a[-3:])
# print()
# print(a[:-2])#-2 not include taken from 0 to -3.
# print()
# print(a[1:4])
# print()
# print(a[0:4])
# print()
# print(a['b'])#We can also fetch values using index values or labels.
# print()
# print(a[['b','c','d','a']])#we can also use multiple labels to fetch values but mention labels inside a square brackets.
# print()

# import pandas as pd

# import numpy as np

# a=pd.Series([1,2,3,4,5,6],index=['a','b','c','d','e','f'])

# print(a.index)#return  the index values of the series

# print()

# print('the axes are:')
# print(a.axes)#it will return the axis(index) of the series.
# print()
# print(a.empty)#it check the given series is empty or not.
# print()
# print(a.ndim)#check for the dimension of the series.
# print()
# print(a.size)#check for the length of the series.
# print()
# print(a.values)#return  the values of the series.
# print()


# import pandas as pd

# import numpy as np

# data=['a','b','c','d','e','f','g','h','i']

# a=pd.Series(data,index=[101,102,103,104,105,106,107,108,109])

# print(a)
# print()
# print(a.head(5))#Head will return the first 5 values.
# print()
# print(a.tail(5))#Tail will return the last 5 values.




#2.DataFrame


#Pandas DataFrame is two-dimensional size-mutable, potentially heterogeneous(more than one type of data) tabular data structure with labeled axes (rows and columns). 
#A Data frame is a two-dimensional data structure, i.e., data is aligned in a tabular fashion in rows and columns.
#DataFrame is like a SQL table.

# A Data frame is a two-dimensional data structure, i.e., data is aligned in a tabular fashion in rows and columns.
# We can perform basic operations on rows/columns like selecting, deleting, adding, and renaming.

# Both represent 'rectangular' data types, meaning that they are used to store tabular data, with rows and columns.
# The main difference, as you'll see, is that matrices can only contain a single class of data, while data frames can consist of many different classes of data.
# Matrix is a 2-dimensional array.#In arrays there is no column or row labels.



# “axis 0” represents rows and “axis 1” represents columns.
# Now it's clear that Series and DataFrame share the same direction for “axis 0” – it goes along rows direction.




# import pandas as pd

# import numpy as np

# pd.DataFrame(data,index,columns,dtype,copy)#A parameter column is comming additional here.


# import pandas as pd

# df=pd.DataFrame()
# print(df)#we get empty dataframe.

# import pandas as pd

# data=[1,2,3,4,5]#here we passing list of values.Result value is always 2 dimensional.
# df=pd.DataFrame(data)#Here (0,1,2,3,4) representing the row index value and 0 above the value (data=1,2,3,4,5) is the column default index value.
# print(df)#This is a 2 dimensional array.
# print(df.values)

# import pandas as pd
# import numpy as np

# data=[['alex',20],['bob',23],['max',14]]

# df1=np.array(data)#In arrays there is no column or row labels.
# print(df1)

# df=pd.DataFrame(data,columns=('Name','Age'),dtype='float')#Here we set column names.we can change data type in dtype.
# print(df)


# Note that in series we are giving index value as column name

# import pandas as pd

# data=[['alex',20],['bob',23],['max',14]]

# df= pd.DataFrame(data,columns=('Name','Age'),dtype='float',index=[101,101,102])
# print(df)


# import pandas as pd

# data={'Name':['alex','bony','bob','max','don'],'Age':[23,33,12,24,32]}#Here the key of the dictionary taken as the column name.

# df= pd.DataFrame(data)
# print(df)



# import pandas as pd

# data={'Name':['alex','bony','bob','max','don'],'Age':[23,33,12,24,32]}#here values passed as a dictionary.
# df= pd.DataFrame(data,index=[10,11,12,13,14])#Here we not need the column name because we use dictionary here so key take as the column name.
# print(df)


# import pandas as pd

# data= [{'a':1,'b':2},{'a':5,'b':10,'c':11},{'a':5,'b':10,'c':11}]#here we give many dictionaries as list.Here we give same key value to multiple dictionaries.
# df= pd.DataFrame(data)#'a' is the first column name,'b' is the second and 'c' is the third column name.
# print(df)             #here first dictionary key value 'c' is empty.so the dataframe also show Nan(NULL).

# import pandas as pd

# data= [{'a':1,'b':2},{'a':5,'b':10,'c':11},{'a':5,'b':10,'c':11}]
# df= pd.DataFrame(data,index=['first','second','third'])
# print(df)




#We can also convert series to dataframe.

# import pandas as pd

# data= {
#         'one':pd.Series([1,2,3],index=['a','b','c']),
#         'two':pd.Series([1,2,3,4],index=['a','b','c','f'])
# }


# df= pd.DataFrame(data)#here we add series as values here.
# print(df)
# print()

# print(df['one'])
# print(type(df['one']))#here we get datatype series,column 'one' is a series.
# print(type(df[['one','two']]))#datatype is  dataframe
# print()
# print(df[['one','two']])


# import pandas as pd

# data={
#     'one':pd.Series([1,2,3],index=['a','b','c']),
#     'two':pd.Series([1,2,3,4],index=['a','b','c','f']),
#     'two':pd.Series([1,2,3,4,5],index=['a','b','c','f','g'])
# }

# df=pd.DataFrame(data)

# print(df)


# print()
# print(df['one']>2)#here checking conditions true or false in the column ways.
# print(df[df['one']>2])#Using this way we can check conditions.



# import pandas as pd

# data ={
#     'one':pd.Series([1,2,3],index=['a','b','c']),
#     'two':pd.Series([1,2,3,4],index=['a','b','c','f'])
# }


# df=pd.DataFrame(data)
# print(df)
# print()

# df['three']=pd.Series([1,2,3,4,5],index=['a','b','c','f','g'])#This way is to append value,same like dictionary.

# print(df)

# df['four']=df['one']+df['two']

# print(df)

# del df['three']#Here we delete values.

# print(df)

# df.pop('two')#Another way to delete values.Here no need to use square brackets.

# print(df)





# import pandas as pd

# data ={
#     'one':pd.Series([1,2,3],index=['a','b','c']),
#     'two':pd.Series([1,2,3,4],index=['a','b','c','f'])
# }

# df=pd.DataFrame(data)
# print(df)
# print()


# print(df.loc['b'])#Here we use loc method to fetch a specific row and column values using row labels or row index(eg:'a','b','c','f').

# print(df.loc['a':'f':2])#we can do slicing of values using log.
# print(df['a':'f':2])
# print(df.iloc[0])#here we can fetch rows and columns using default index value.0 fetch the 0th row index values.
# print(df.values)
# print(df.iloc[0:3])#fetch values from 0 t0 3rd row


#Slicing of Dataframe


# import pandas as pd

# data ={
#     'one':pd.Series([1,2,3],index=['a','b','c']),
#     'two':pd.Series([1,2,3,4],index=['a','b','c','d']),
#     'three':pd.Series([1,2,3,4],index=['a','b','c','d'])
# }


# df=pd.DataFrame(data)
# print(df)

# print(df[1:])#take values from row index 1 to last index from each rows.
# print()
# print(df[1:3])
# print()
# print(df[-1:])#values taken from -1 index of row,that is last value only.
# print()
# print(df[:-1])#Here -1 index value exclude and take the rest.
# print()

# print(df[1:4:2])
# print()


# print(df[::])
# print()

# print(df.ndim)

# print(df['a'])
# print(df.values)
# print(df['a':'c'])

# print(df[['one','three']])


# import pandas as pd

# df1=pd.DataFrame([[2,3],[4,5]],columns=['col1','col2'])
# df2=pd.DataFrame([[6,7],[8,9]],columns=['col4','col5'])

# print(df1)
# print()
# print(df2)
# print()

# print(df1.append(df2))#Here we append a Dataframe to another using append method.  
#                       #if we append a Dataframe with different column name then that column part of first dataframe show NuN(NULL) and vise versa.


# import pandas as pd

# df1=pd.DataFrame([[2,3],[4,5]],columns=['col1','col2'])
# df2=pd.DataFrame([[6,7],[8,9]],columns=['col1','col2'])

# df=df1.append(df2)

# print(df)
# print(df.values)
# print(df.drop(0))#here 0th index position rows will clear from both rows.if we specifies row index, then the row delete only if we mention that index.Here defaultly delete 0th index.


# import pandas as pd

# data=[[1,2,3],[4,5,6]]

# data1=[[7,8,9],[10,11,12]]
# df1=pd.DataFrame(data,index=[0,2],columns=['col1','col2','col3'])
# df2=pd.DataFrame(data1,index=[1,4],columns=['col1','col2','col3'])
# df=df1.append(df2)

# print(df1)

# print(df.drop(0))

# print(df.drop(index=df.index[:3]))#Here we can mention how many rows to delete using the attribute 'index'.




#We can use heterogenous(not same type of data we can use integer,string... as values) type of datas in dataframe and series.


# import pandas as pd

# d={
#     'Name':pd.Series(['tom','james','nik','smith','john','don','roky']),
#     'Age':pd.Series([23,22,21,14,23,35,36]),
#     'Rating':pd.Series([3.7,3.6,2.5,4.7,3.8,3.5,4.2])
#     }

# df=pd.DataFrame(d)
# print(df)
# print()
# print(df.T)#Here 'T' means Transpose,that means rows become columns and columns become rows. 
# print()
# print(df.ndim)
# print()
# print(df.dtypes)

#A data type object (an instance of numpy. dtype class) describes how the bytes in the fixed-size block of memory corresponding to an array item should be interpreted.
# It describes the following aspects of the data: Type of the data (integer, float, Python object, etc.)

# print()
# print(df.columns)#here we get column labels.
# print()
# print(df.values)#it shows the values in an array format.
# print()
# print(df.empty)
# print()
# print(df.head(5))#fetch first 5 rows.
# print()
# print(df.tail(5))#fetch last 5 rows.
# print()
# print(df.axes)#axes means index


#Statistical Operations


# import pandas as pd

# d={
#     # 'Name':pd.Series(['tom','james','nik','smith','john','don','roky']),
#     'Age':pd.Series([23,22,21,14,23,35,36]),
#     'Rating':pd.Series([3.7,3.6,2.5,4.7,3.8,3.5,4.2])
#     }

# df=pd.DataFrame(d)

# # print(df)
# # print()
# # print(df.mean())
# # print()
# # print(df.median())
# # print()
# print(df.mode())

#The mode is the value that appears most frequently in a data set.
# A set of data may have one mode, more than one mode, or no mode at all.
# Other popular measures of central tendency include the mean, or the average of a set, and the median, the middle value in a set.


# print()
# print(df.std())#std is the standard Deviation.
# print()
# print(df.min())
# print()
# print(df.max())
# print()
#print(df.describe())       ##In describe we get overall result that include mean,median,std,max,min,count...
# print(df.cumsum(axis=0))   #here we can find cumulative sum.In cumulative sum is suming up of values and in last column we get overall sum.axis=0 means row based and axis= 1 means column based.
# print()
# print(df.count())#Count total values in a label(column index)



#######################################################################################################################

#Nested chaining

# f(g(h(df), arg1=a), arg2=b, arg3=c)


#In the documentation of pandas, there are 3 functions: h(df), g(df,arg1=a), f(df,arg2=b, arg3=c) applied on df in this order.
# Usually, three functions are nested in the sequence of calling.
# It is hard to read the functions & arguments at first glance.
# By method chaining, the relationships among operations can be shown in a clearer format.


##Method Chaining


# df.pipe(h)
# df.pipe(g, arg1=a)
# df.pipe(f, arg2=b, arg3=c)





#Pipe is a method in pandas. DataFrame capable of passing existing functions from packages or self-defined functions to dataframe.
# It is part of the methods that enable method chaining. By using pipe, multiple processes can be combined with method chaining without nesting.

#Nested Loop


#A nested loop is a loop inside the body of the outer loop. 
# The inner or outer loop can be any type, such as a while loop or for loop.
# For example, the outer for loop can contain a while loop and vice versa.



# import pandas as pd

# def addval(elem,num):#here 'elem' get the  each values from the dataframe and 'num' get the value 2.
#     return elem+num

# df1=[[1,2],[3,4],[5,6],[7,8],[9,10]]
# df=pd.DataFrame(df1,columns=['col1','col2'])
# print(df)
# print()
# print(df.pipe(addval,2))#pipe is a inbuilt method in dataframe to add dataframe value  with a number.
#                       #Here pipe function fetch each values from the dataframe.

# print(addval(df,2))#above is same like this method(here we use nested function),for doing easy to undesrstand we use method chaining.



# import pandas as pd

# import numpy as np

# df1=[[1,2],[3,4],[5,6],[7,8],[9,10]]
# df=pd.DataFrame(df1,columns=['col1','col2'])
# print(df)
# print()
# print(df.apply(np.mean,axis=0))#Here we calculate mean based on column.
# print()
# print(df.apply(np.mean,axis=1))#Here we calculate mean based on row.By default mean based on column.
# print()
# print(df.apply(np.mean))
# print()
# print(df.applymap(lambda x:x*100))#applymath used to apply functions using lambda function(column based multiply values).
# print(df.apply(np.median,axis=0))
# print(df.median(0))



#Sorting 


# import pandas as pd

# import numpy as np

# df=pd.DataFrame(np.random.rand(10,2),index=[1,4,7,2,3,8,9,10,5,6])#combination of 10 1 d array with 2 column,float value between 0-1.
# print(df)
# print()
# sorted=df.sort_index()#sort_index used to sort the row index values.
# print(sorted)
# print()
# sorted=df.sort_index(ascending=False)#Here 'ascending=False' so it fetch index values in descending order we can also do in vise-versa.
# print(sorted)
# print()


# import pandas as pd

# import numpy as np

# df=pd.DataFrame(np.random.rand(10,2),index=[1,4,7,2,3,8,9,10,5,6],columns=['col1','col2'])#combination of 10 1 d array with 2 column,float value between 0-1.
# print(df)
# sorted=  df.sort_values(by=['col1'])#'sort_values' used labels(column index to sort values)
#                                     #by used to mention which column to sort.
# print(sorted)
# sorted=df.sort_values(by=['col1'],ascending=False)
# print(sorted)




# import pandas as pd

# import numpy as np

# df=pd.DataFrame(np.random.rand(10,2),index=[1,4,7,2,3,8,9,10,5,6],columns=['col1','col2'])#combination of 10 1 d array with 2 column,float value between 0-1.
# print(df)
# print()
# sorted=  df.sort_values(by=['col1'],kind='mergesort')#In attribute 'kind' we can mention which type of sorting.
# print(sorted)
# print()
# sorted=  df.sort_values(by=['col1'],kind='headsort')
# print(sorted)
# print()
# sorted=  df.sort_values(by=['col1'],kind='quicksort')
# print(sorted)
# print()



# import pandas as pd

# import numpy as np

# df=pd.DataFrame(np.random.rand(5,3),index=['a','c','e','f','h'],columns=['one','two','three'])
# print(df)
# print()
# df=df.reindex(['a','b','c','d','e','f','g'])#Here we use 'reindex' method to set new index values, the non existing index values will add to the position ways and already existing remains same.
#                                             #New index values set with NaN(NULL) values.
# print(df)
# print()
# print(df['one'].isnull())#Used to check the column values is NULL(Shows True) or not NULL(shows False).Here we get a boolean value.
# print()
# print(df['one'].notnull())#opposite way of isnull.
# print()



# print(df.fillna(3.4))#fillna used to fill the null(NaN) values.

# print()

# print(df.fillna(method='pad'))#This is forward filling of values,first row values use to fill the 2nd null row values here,
#                               #4th row filled using 3rd row values.
# print()
# print(df.fillna(method='bfill'))#backward filling just like forward filling but start from the last row.

# print()
# print(df.dropna())#dropna used to remove the empty rows.


# import pandas as pd

# import numpy as np



# d={'Name':['a','b','c','d','a'],'Age':[12,23,34,45,45]}
# df=pd.DataFrame(d)
# print(df.values)
# print()

# How do you Count the Number of Occurrences in a data frame?
# To count the number of occurrences in e.g. a column in a dataframe you can use Pandas value_counts() method.
# For example, if you type df['condition'].value_counts() you will get the frequency of each unique value in the column “condition”.

# print(df['Name'].value_counts())

# print(df.replace({12:22,34:33}))#replace method is used to replace a columnvalues with new values.

# print(df.replace({'a':'qw','b':'iu','c':'hj','d':'hj'}))#We can only replace one column values at a time.




#Group By


# import pandas as pd

# import numpy as np


# data = {'Team':['Riders','Riders','Devils','Devils','Kings','Kings','Kings',
#                       'Kings','Riders','Royals','Royals','Riders'],
#     'Rank':[1,2,2,3,3,4,1,1,2,4,1,2],
#     'Year':[2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
#     'Points':[725,826,825,930,732,621,731,534,473,823,933,856]
#     }


# df=pd.DataFrame(data)
# print(df)
# print()
# grouped=df.groupby('Team')#'groupby' used to group similar values.Here grouped is an object so,we need to iterate(loop) it.
# for Team_name,Team_df_name in grouped: #Here 'Team_name' is the grouped team name and 'Team_df_name' is the dataframe of the grouped Team_names.
#     print('Name:',Team_name)
#     print('Group:\n')
#     print(Team_df_name)
#     print()
# print(grouped.get_group('Riders'))
# print(grouped)

# df=pd.DataFrame(data)
# print(df)
# print()
# grouped=df.groupby('Year')#'groupby used to group similar values.
# for name,group in grouped:
#     print('Name:',name)
#     print('Group:\n')
#     print(group)
#     print()

# print(grouped.get_group(2014))#get_group used to get a value of  specific condition(eg:same year) only.



# Merge


import pandas as pd

import numpy as np





# left = pd.DataFrame({
#     'id':[1,2,3,4,5],
#     'Name':['alex','amy','allen','alice','aion'],
#     'subject_id':['sub1','sub2','sub3','sub4','sub5']})

# right = pd.DataFrame({
#     'id':[1,2,3,4,5],
#     'Name':['billy','brain','bran','bryce','betty'],
#     'subject_id':['sub2','sub4','sub3','sub6','sub5']})

# print(pd.merge(left,right,on='id'))#'merge' function used to merge two dataframes based on a common column values(basically get like the left inner join in sql).
# print()
# print(pd.merge(right,left,on='id'))
# print()
# print(pd.merge(left,right,on=['id','subject_id']))#Here two dataframes should same column values(basically get like the right inner join in sql) of two column indexs.
# print()
# print(pd.merge(right,left,on=['id','subject_id']))



# Concatenate #it means merging.


#pandas.concat(objs, axis=0, join='outer', ignore_index=False, keys=None, levels=None, names=None, verify_integrity=False, sort=False, copy=True)






import pandas as pd

import numpy as np





# one = pd.DataFrame({
#     'id':[1,2,3,4,5],
#     'Name':['alex','amy','allen','alice','aion'],
#     'subject_id':['sub1','sub2','sub3','sub4','sub5'],
#     'marks_scored':[84,87,88,78,97]},
#     index=[1,2,3,4,5])

# two = pd.DataFrame({
#     'id':[1,2,3,4,5],
#     'Name':['billy','brain','bran','bryce','betty'],
#     'subject_id':['sub2','sub4','sub3','sub6','sub5'],
#     'marks_scored':[82,85,81,71,91]},
#         index=[1,2,3,4,5])


# print(pd.concat([one,two],ignore_index=False,axis=1)) #column based

# print(pd.concat([one,two],ignore_index=True,axis=0)) #row based based


# print()

# print(one.append(two))




# import pandas as pd

# import numpy as np




# left = pd.DataFrame({
#     'id':[1,2,3,4,5],
#     'Name':['alex','amy','allen','alice','aion'],
#     'subject_id':['sub1','sub2','sub3','sub4','sub5']})

# right = pd.DataFrame({
#     'id':[1,2,3,4,5],
#     'Name':['billy','brain','bran','bryce','betty'],
#     'subject_id':['sub2','sub4','sub3','sub6','sub5']})

# print(pd.merge(left,right,on='subject_id',how='left'))#Here merge based on left inner join(same like in sql).
# print()
# print(pd.merge(left,right,on='subject_id',how='right'))
# print()
# print(pd.merge(left,right,on='subject_id',how='inner'))
# print()
# print(pd.merge(left,right,on='subject_id',how='outer'))


#######################################################################################################################

'''Question 1'''



#df = pd.DataFrame({'Animal':['Falcon','Falcon','Parrot','Parrot'],'Max_speed':[380,370,24,26]})


'''Question 2'''


#df=pd.read_csv("http://bit.ly/drinksbycountry%22)
# print(df)

# find the average of each continent by grouping the data based on th 'continent'.
# sum,min and max of column beer_servings is to be calculated
# find an aggregation of column "beer_servings" by grouping the "continent" column.

#########################################################################################################################

# import pandas as pd

# iris=pd.read_csv('Iris.csv')
# print(iris)


# ds=iris.copy()#Copying to avoid any errors occur in the main file.

# print(ds)



''' Question 3'''

# select sepal length
# select sepal and petal length
# select all values with sepal length>5cm
# create a new column which is TotalpetalCm=PetalLengthCm+PetalWidthCm
# Delete column TotalPetalCm from dataset
# Access the dataframe using iloc the first 10 records
# delete the first row from the dataframe
# delete the first 10 rows from the dataframe
# Reindex the dataframe
# use the describe function
# finid the sentos,verginaca and vericolor flowe describe them separately
# sort the dataframe according to SepalLengthCm

# Rename the PetalLengthCm column as PL(Cm),SepalwidthCm as AW(Cm) and 
# PetalWidthCm as PW(Cm).

# Rename SepalLengthCm as SP(Cm)
# find and print count of each kind of flower.print the count as integer value
# Find the data of flower "iris-virginiva" tupe where petal-length>1.5


############################################################################################################################


'''Question 1'''

# identify the Sum of Falcon.


# import pandas as pd

# import numpy as np


# df = pd.DataFrame({'Animal':['Falcon','Falcon','Parrot','Parrot'],'Max_speed':[380,370,24,26]})

# df1=df.copy()

# grouped=df1.groupby('Animal')


# for name,group in grouped:
#     if name=='Falcon':
#         a=group.values
#         b=sum(a[:,1])
# print('Sum of Falcon is:',b )
# print()


# 'OR'

# a=grouped.get_group('Falcon')
# print()
# b=a.values
# print(b)
# c=sum(b[:,1])
# print(b)
# print('Sum of Falcon is:',c)
      

############################################################################################################################

'''Question 2'''


#df=pd.read_csv("http://bit.ly/drinksbycountry%22)
# print(df)

# find the average of each continent by grouping the data based on the 'continent'.
# sum,min and max of column beer_servings is to be calculated
# find an aggregation of column "beer_servings" by grouping the "continent" column.



# import pandas as pd

# df=pd.read_csv('http://bit.ly/drinksbycountry%22')#we can also read a csv_file using pandas.
# print(df)

        
# ds=df.copy()

# print(ds)

# ds1=pd.DataFrame(ds)
# print(ds1)


# grouped=(ds1.groupby('continent').mean())#here grouped is an object.

# print(grouped)
# print()
# a=grouped['beer_servings'].agg(['sum','min','max'])

# print(a)


#agg()-aggregate function
#Here we need to mention the sum etc inside a list.
#Aggregate the values of a column in the current table.
#The following aggregation functions are available: Average, Count, Maximum, Median, Minimum, Predominant, Standard deviation, Sum.
# All aggregation functions can be used to aggregate the values of a whole column: you obtain one output value.

######################################################################################################################################################################################################



'''Question 3'''


# select sepal length
# select sepal and petal length
# select all values with sepal length>5cm
# create a new column which is TotalpetalCm=PetalLengthCm+PetalWidthCm
# Delete column TotalPetalCm from dataset
# Access the dataframe using iloc the first 10 records
# delete the first row from the dataframe
# delete the first 10 rows from the dataframe
# Reindex the dataframe
# use the describe function
# find the setosa,virginica and versicolor flower describe them separately
# sort the dataframe according to SepalLengthCm

# Rename the PetalLengthCm column as PL(Cm),SepalwidthCm as SW(Cm) and 
# PetalWidthCm as PW(Cm).

# Rename SepalLengthCm as SP(Cm)
# find and print count of each kind of flower.print the count as integer value
# Find the data of flower "iris-virginica" tupe where petal-length>1.5



# import pandas as pd

# df=pd.read_csv('D:/Download files/Iris.csv')
# print(df)

# df1=df.copy()

# ds=pd.DataFrame(df1)

# print(ds)

# sepallen=ds['SepalLengthCm']

# petallen=ds['PetalLengthCm']

# print(sepallen[sepallen>5])

# TPL=ds['PetalLengthCm']+ds['PetalWidthCm']

# TotalPetalCm=pd.DataFrame(TPL)

# ds['TotalPetalCm']=TotalPetalCm

# print(ds)

# del ds['TotalPetalCm']

# print(ds)

# print(ds.iloc[0:10])

# print(ds.drop(0))

# print(ds.drop(index=ds.index[:10]))

# grouped=ds.groupby('Species')

# dessetosa=grouped.get_group('Iris-setosa').describe()
# print(dessetosa)
# print()
# desvir=grouped.get_group('Iris-virginica').describe()
# print(desvir)
# print()
# desversi=grouped.get_group('Iris-versicolor').describe()
# print(desversi)


# print(ds.sort_values(by=['SepalLengthCm']))

# ds_new=ds.rename(columns={'SepalLengthCm':'SL(Cm)','SepalWidthCm':'SW(Cm)','PetalLengthCm':'PL(Cm)','PetalWidthCm':'PW(Cm)'})#This is the way to rename the label names.
# print(ds_new)

# print(ds_new['Species'].value_counts())

# print()

# ds_new1=ds_new[ds_new['PL(Cm)']>1.5]

# print(ds_new1)

# grouped=ds_new1.groupby('Species')

# PLvir=grouped.get_group('Iris-virginica')
# print(PLvir)

##################################################################################################################################################################################