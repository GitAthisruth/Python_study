from unittest.mock import patch  # used to mock an object

# we can also use patch as a decorator.

# tests should be isolated

# test driven development - we write the test code before we write the code.

# to test the file just print it for unittest.

import unittest

# from unittest import TestCase

from class_unit import Employee


class TestEmployee(unittest.TestCase):
    @classmethod  # used to convert a function to a class method.
    def setUpClass(cls):  # also used to connect with a server.
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    def setUp(self):
        print("setUp")
        self.emp_1 = Employee("Corey", "Schafer", 50000)
        self.emp_2 = Employee("Sue", "Smith", 60000)

    def tearDown(self):
        print("tearDown\n")

    def test_email(self):
        print("test_email")
        self.assertEqual(self.emp_1.email, "Corey.Schafer@email.com")
        self.assertEqual(self.emp_2.email, "Sue.Smith@email.com")

        self.emp_1.first = "John"
        self.emp_2.first = "Jane"

        self.assertEqual(self.emp_1.email, "John.Schafer@email.com")
        self.assertEqual(self.emp_2.email, "Jane.Smith@email.com")

    def test_fullname(self):
        print("test_fullname")

        self.assertEqual(self.emp_1.fullname, "Corey Schafer")
        self.assertEqual(self.emp_2.fullname, "Sue Smith")

        self.emp_1.first = "John"
        self.emp_2.first = "Jane"

        self.assertEqual(self.emp_1.fullname, "John Schafer")
        self.assertEqual(self.emp_2.fullname, "Jane Smith")

    def test_apply_raise(self):
        print("test_apply_raise")

        self.emp_1.apply_raise  # it change the 50000 in the object to 52500.
        self.emp_2.apply_raise

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

        # here class unit is the file module(eg:class_unit) that we import for testing.

    def test_monthly_schedule(self):
        with patch("class_unit.requests.get") as mocked_get:
            # here we are just making a mock object to check  that it is working or not.
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = (
                "Success"  # here we set a values as "Success".
            )

            schedule = self.emp_1.monthly_schedule("May")
            mocked_get.assert_called_with("http://company.com/Schafer/May")
            self.assertEqual(schedule, "Success")

            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule("June")
            mocked_get.assert_called_with(
                "http://company.com/Smith/June"
            )  # used to call url correctly.
            self.assertEqual(schedule, "Bad Response")


if __name__ == "__main__":
    unittest.main()


# setUp() and tearDown() are two special methods in the unittest.TestCase class in Python that allow you to set up and clean up resources before and after each test method is run.

# In the given code snippet, setUp() method is initializing two Employee objects, emp_1 and emp_2, with some sample data. This is useful for reducing code duplication, as these objects will be used in multiple test methods.

# tearDown() method is not doing anything here, as it is empty. However, it could be used to clean up any resources that were created during the test, such as closing a database connection or deleting a temporary file.

# Overall, setUp() and tearDown() methods can be used to set up a known state for each test, which can help ensure that tests are predictable and reproducible.


# The setUpClass() method is called once before any of the test methods in the class are run, and it is typically used to set up any resources that will be shared across all test methods in the class. For example, if you have a test class that needs to connect to a database, you could use setUpClass() to establish the database connection, so that it doesn't need to be established separately in each test method.

# Similarly, the tearDownClass() method is called once after all the test methods in the class have been run, and it is used to clean up any resources that were created during the tests. For example, if you used setUpClass() to establish a database connection, you could use tearDownClass() to close the connection and release any associated resources.


# In general, mocking is a technique used in testing to replace a real object with a "mock" object that behaves like the real object, but is under the control of the test. Mocking can be useful in cases where the real object is difficult to set up, unreliable, or has side effects that could affect other parts of the system.


# mocked_get.assert_called_with("http://company.com/Schafer/May"): This assertion checks whether a mocked get() method was called with the argument "http://company.com/Schafer/May". If the method was not called with this argument, the test will fail.
