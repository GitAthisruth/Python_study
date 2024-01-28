# Pytest

# It is  a frame work to test a code.



# we can test the code in parallel mode.

# Suite - Set of testcases

# Precondition - Postcondition

#pytest can identify the test files with name start with or end with name "test".

#we need to give the test file with name  start with or end with test.


#Here we can use #pytest command in the terminal to start testing the files.

# we can also use #py.test

#pytest -rA  this command gives as the full details of the test files.

#  # pytest test_first.py -rA -k login

# -used to scan all test files and check the function only we want.

#    k-used to check only a specific function

# -rA -used to scan all the test files 

# -rA -run all the test

#-v -verbose for more information


#pytest -rA --junitxml="Report1.x" -to save our test report as an xml file.


# Parameterizing of a test is done to run the test against multiple sets of inputs. We can do this by using the following marker − @pytest.mark.parametrize. 