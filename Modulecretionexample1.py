def ath(k):
    sum=0
    for i in k:
        sum+=i
    return sum




print(__name__)


if __name__=='__main__':
    print(ath([1,2,3,4]))


#when we mention this code,

#then this fuction call execute only in here.


#this will not execute when we call this python file as a module in another python file.

# In that case,__name__==ath,so if condition not satisfy.ie,it will not true.
# Then the function call print(ath([1,2,3,4])) not execute.


# in this filev __name__ == main

# But in the file that we import this, __name__ == 'function_name(eg:ath)


#Here the __name__ denoting the environmental variable name(filename).

#Then,this file is the main file.
#So,if condition will true.so,the function will execute.

# if we execute this python file as a module in another file.
# Then it is not the main file so it will not execute the function call inside the if condition. 