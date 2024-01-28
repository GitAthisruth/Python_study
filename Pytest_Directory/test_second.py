

def test_1():
    x = 0
    y = 0
    assert x == y



def test_2():

    name = "Selenium"

    title = "Selenium is for web automation"
    assert name in title


def test_3():

    name = "Selenium"

    title = "Selenium is for web automation"
    assert name in title  , "name does not match"