
def add(x,y):
    """Add Function"""
    return x+y

def subtract(x,y):
    """Subtract Function"""
    return x-y

def multiply(x,y):
    """multiply Function"""
    return x*y

def divide(x,y):
    """divide Function"""
    if y==0:
        raise ValueError("Cannot divide a number with zero")
    return x/y


