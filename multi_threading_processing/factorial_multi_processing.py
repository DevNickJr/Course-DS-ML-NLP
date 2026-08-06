import multiprocessing
import time
import math
import sys

sys.set_int_max_str_digits(1000000)

def factorial(n):
    print(f'factorial {n}')
    return math.factorial(n)

if __name__ == '__main__':
    numbers = [190000,190000,190000,190000]
    with multiprocessing.Pool() as pool:
        results = pool.map(factorial, numbers)
    print(results)
    for result in results:
        print(result)
