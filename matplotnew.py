
#Matplotlib is a cross-platform, data visualization and graphical plotting library for Python and its numerical extension NumPy.
#As such, it offers a viable open source alternative to MATLAB. Developers can also use matplotlib's APIs (Application Programming Interfaces) to embed plots in GUI applications




import matplotlib.pyplot as plt

import numpy as np



x=np.arange(0,10)
print(x)

#we should give equal length in x and y axis ,otherwise throw error.

y=np.arange(11,21)

plt.figure()#Create a new figure, or activate an existing figure, using plt.figure().

plt.scatter(x,y,c='b')##'b' representing colour blue.we can set color in variable c here.

#Scatter plots are the graphs that present the relationship between two variables in a data-set.
#It represents data points on a two-dimensional plane or on a Cartesian system. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.



plt.title('scatter plot')

plt.xlabel('xaxis')

plt.ylabel('yaxis')

# plt.savefig('sample2.png')

plt.show()


# x=np.arange(0,10)

# y=x*x
# print(y)
# plt.plot(x,y,'r*--',linewidth=5,markersize=20)#here r represent the color red,'*' and '--' represent the star and - in the graph.
#                                               #linewidth represent the width of the graph line.markersize is the size of given pattern(here we give star)
# plt.title('2nd plot')
# plt.xlabel('xaxis')
# plt.ylabel('yaxis')

# plt.show()


# x=np.arange(0,10)
# y=x*x
# print(y)
# plt.plot(x,y,'r*--',linewidth=5,markersize=20)
# plt.title('2nd plot')
# plt.xlabel('xaxis')
# plt.ylabel('yaxis')

# plt.show()



# x=np.arange(0,10)
# y=x*x


# plt.subplot(2,2,1)#Here (2,2) means row and column. 1 is representing the subplots number.we should give it correctly otherwise it throw error.

# plt.plot(x,y,'r')
# plt.subplot(2,2,2)

# plt.plot(x,y,'g')
# plt.subplot(2,2,3)

# plt.plot(x,y,'b')
# plt.subplot(2,2,4)

# plt.plot(x,y,'y')

# plt.show()



#y=mx+c  ##equation of the straight line.


# x=np.arange(0,10)

# y=3*x + 5

# plt.plot(x,y)#By default, the plot() function draws a line from point to point.


# plt.show()



# print(np.pi)#here we get the pie value.

# x=np.arange(0,4*np.pi,0.1)#0.1 is the common difference here.
# y=np.sin(x)

# plt.plot(x,y,'y')#by default we get blue color.
# plt.show()



# x=np.array([2,4,5,55,77,12,66,89,98,45,90,99])

# plt.hist(x,'auto',ec='black')#'ec' means 'edge color',

# #A histogram is a graphical representation that organizes a group of data points into user-specified ranges.
# #Similar in appearance to a bar graph, the histogram condenses a data series into an easily interpreted visual by taking many data points and grouping them into logical ranges or bins.
# #Can display large set of data.
# #Here each bars represent a range of x values,y represents the count of values. 


# plt.title('histogram')
# # plt.xticks(x) #we can know values taken in x axis.we can also set y values seperately here.
# plt.show()#Here each bars known as  bin.


# data = [np.random.normal(0,res,100) for res in range(1,4)]


#Normal distribution, also known as the Gaussian distribution, 
#is a probability distribution that is symmetric about the mean, showing that data near the mean are more frequent in occurrence than data far from the mean. 
#In graph form, normal distribution will appear as a bell curve.
# In statistics, the mode is the most commonly observed value in a set of data.
# For the normal distribution, the mode is also the same value as the mean and median.
# In many cases, the modal value will differ from the average value in the data.





# print(data)

# plt.boxplot(data)

# plt.show()


# A Box Plot is also known as Whisker plot is created to display the summary of the set of data values having properties like minimum, first quartile, median, third quartile and maximum.

# In the box plot, a box is created from the first quartile to the third quartile, a vertical line is also there which goes through the box at the median.

# Here x-axis denotes the data to be plotted while the y-axis shows the frequency distribution.






############################################################################################################


#pyDiagram(piechart)

#Use matplotcheat sheets in google to see different graphs structures with codes.


# y = np.array([35, 25, 25, 15])

# plt.pie(y)
# plt.show() 




# label='python','java','c++','ruby' 

# size=[215,130,245,210]#java is the largest one and java is smallest.We can give values in tuple also.

# colors=['red','yellowgreen','lightcoral','lightskyblue']#Give correct order for label and colors to get correct order of colors.
# explodes=(0.4,0,0,0.6)  #To “explode” a pie chart means to make one of the wedges of the pie chart to stand out.
#                         #To make this possible in matplotlib, we use the explode() parameter.

# plt.pie(size,explode=explodes,labels=label,colors=colors,shadow=True)#shadows give shadow to the pie chart.
# plt.show()