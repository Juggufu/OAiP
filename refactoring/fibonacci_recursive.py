import cProfile
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

import functools


@functools.lru_cache()
def fibonacci_recursive(number):
    if number <= 1:
        return number
    return fibonacci_recursive(number - 1) + fibonacci_recursive(number - 2)

def fibonacci_recursive(number):
    if number == 0:
        return 0
    elif number == 1 or number == 2:
        return 1
    else:
        return fibonacci_recursive(number - 1) + fibonacci_recursive(number - 2)


cProfile.run('fibonacci_recursive(30)')