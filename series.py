"""Define fibonacci and lucas function"""


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


def sum_series(n, a=0, b=1):
    """make function that work with both lucas and fibonacci"""
    if n == 1:
        return a
    if n == 2:
        return b
    return sum_series(n - 2, a, b) + sum_series(n - 1, a, b)
