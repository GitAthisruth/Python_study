import unittest#here we import the unittest module
import calcul_unit #then import the file(module) for testing 


# print(calcul_unittest.add(78,90))
# print(calcul_unittest.multiply(78,90))
# print(calcul_unittest.multiply(788,90))

# test case
# A test case is the individual unit of testing. It checks for a specific response to a particular set of inputs. unittest provides a base class, TestCase, which may be used to create new test cases.

# In the example code class TestStringMethods(unittest.TestCase):, we named the parent class unittest.TestCase because we want to use the TestCase class provided by the unittest module as the parent class for our test case.

class TestCalc(unittest.TestCase):#here we inheritting the methods and variable from the parent class unittest.TestCase.
      def test_add(self):
            self.assertEqual(calcul_unit.add(10,5),15)
            self.assertEqual(calcul_unit.add(1,-1),0)
            self.assertEqual(calcul_unit.add(-1,-1),-2)


      def test_subtract(self):
            self.assertEqual(calcul_unit.subtract(10,5),5)
            self.assertEqual(calcul_unit.subtract(1,-1),2)
            self.assertEqual(calcul_unit.subtract(-1,-1),0)
            
   
      def test_multiply(self):
            self.assertEqual(calcul_unit.multiply(10,5),50)
            self.assertEqual(calcul_unit.multiply(1,-1),-1)
            self.assertEqual(calcul_unit.multiply(-1,-1),1)
            
     
      def test_divide(self):
            self.assertEqual(calcul_unit.divide(10,5),2)
            self.assertEqual(calcul_unit.divide(1,-1),-1)
            self.assertEqual(calcul_unit.divide(-1,-1),1)
            self.assertEqual(calcul_unit.divide(5,2),2.5)

            with self.assertRaises(ValueError):
                  calcul_unit.divide(10,0)

            

if  __name__ =="__main__":#here we giving this condition because this function only execute here if __name__=__main__.This is the main file so this value is not pass to the other files if we import this file to there.
      unittest.main()

# The final block shows a simple way to run the tests. unittest.main() provides a command-line interface to the test script. When run from the command line, the above script produces an output that looks like this:

print(__name__)#it is an environmental variable name(file name).


# In the context of unit testing with the unittest module, the unittest.main() function is used to discover and run all test cases in the current module. By placing unittest.main() inside the if __name__ == "__main__": block, we ensure that the test runner is only executed if the current module is being run as the main program, rather than being imported into another module.

# So the overall purpose of the code if __name__ == "__main__": unittest.main() is to run all the test cases in the current module when the module is run as the main program.