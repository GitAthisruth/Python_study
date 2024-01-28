a = 33
b = 200
global c
c = 5


def debugfun():
    print(4 + 5)


debugfun()
if b > a:
    print("b is greater than a")
    print(c)

    # continue - program will run normally.

    # step over - When you choose to “step over” while debugging, the debugger will execute the current line of code and pause on the next line, without entering any function calls that might be present on the current line.

    # step into - Step Into is used for debugging the test steps line by line.

    # restart - re-run the debugger

    # stop - stop the debugger
