import requests
import pytest
from pytest_with_unit_testing_function import Calculator,MockAPI

def test_calculator():
    # Create a mock API
    mock_api = MockAPI(5)
    # Create the calculator with the mock API
    calculator = Calculator(mock_api)
    
    # Test the add_numbers method
    result = calculator.add_numbers(10)
    
    # Verify the result
    assert result == 15


import unittest.mock as mock
import math_fun

def test_add():
    with mock.patch('pytest_with_unit_testing_learnin.math_fun.add') as mock_add:
        mock_add.return_value = 100

        result = math_fun.add(50, 50)

        assert result == 100