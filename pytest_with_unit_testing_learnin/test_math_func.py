from pytest_with_unit_testing_learnin import math_fun
import pytest


@pytest.mark.number
def test_add():
    assert math_fun.add(7, 3) == 10
    assert math_fun.add(7, 8) == 15
    assert math_fun.add(7, 0) == 7


@pytest.mark.number
def test_product():
    assert math_fun.product(4, 5) == 20
    assert math_fun.product(5, 5) == 25
    assert math_fun.product(4, 0) == 0
    assert math_fun.product(1, 5) == 5


@pytest.mark.number
def test_add_q():
    assert math_fun.add(2, 3) == 5


@pytest.mark.string
def test_add_strings():
    result = math_fun.add("hello ", "world")
    assert result == "hello world"
    assert type(result) is str
    assert "hel" in result


@pytest.mark.string
def test_product_strings():
    assert math_fun.product("Hello ", 3) == "Hello Hello Hello "
    result = math_fun.product("Hello ")
    assert result == "Hello Hello "
    assert type(result) is str
    assert "Hello" in result


"""python -m pytest -vs -m "number" pytest_with_unit_testing_learnin/test_math_func.py -code to test specific  tests of functions only"""
