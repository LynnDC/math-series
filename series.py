""" Define fibonacci and lucas function"""


def fibonacci(n):
    """def fibonacci function using recursion"""
    if n <= 1:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


def lucas(n):
    """lucas function using recursion"""
    if n == 0:
        return 2
    elif n == 1:
        return 1
    return lucas(n - 2) + lucas(n - 1)