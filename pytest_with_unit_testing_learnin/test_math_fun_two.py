from pytest_with_unit_testing_learnin import math_fun
import pytest
'''python -m pytest -v -code to test all pytests'''


@pytest.mark.parametrize(
    "num1,num2,result",
    [("Hello ", "World", "Hello World"), (3, 4, 7), (2.5, 2.5,5)],
)  # using same function we can check the result of many test
def test_add(num1, num2, result):
    assert math_fun.add(num1,num2) == result
