""" Define fibonacci and lucas function"""


def fibonacci1(n):
    """def fibonacci function using recursion"""
    if n <= 1:
        return n
    return fibonacci1(n-2) + fibonacci1(n-1)

