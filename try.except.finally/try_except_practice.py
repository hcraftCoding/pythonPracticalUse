"""
Practice 1: try/except/finally basics


def divide_numbers(a, b):
    # write a try/except/finally block that:
    # - tries to divide a by b
    # - catches ZeroDivisionError with a clean message
    # - always prints "calculation attempted" in the finally block
    pass
"""
def divide_numbers(a, b):
    try:
        c = a / b
        print(c)  #had to be corrected here
    except ZeroDivisionError:
        print("Can't divide by zero in Python")
    finally:
        print("Calculation attempted")
   

    divide_numbers(10, 2)
divide_numbers(10, 0)