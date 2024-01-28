#Every python file is act as a module. 
import Modulecretionexample1

print(Modulecretionexample1.ath([1,2]))

 
# Here this fuction from the module also execute print(ath([1,2,3,4])).
# To avoid that execution 

# we can use this code inside the module file, 

# if __name__=='__main__':
#     print(ath)

#Here the environmental variable name is Modulecretionexample1.
#Also this is not the main file.
#So the if condition will not satisfy and the function call will not execute. 