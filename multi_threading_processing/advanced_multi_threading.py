from concurrent.futures import ThreadPoolExecutor
import time

def print_num(number):
    time.sleep(1)
    return number

numbers = [1,2,3,4,5,6,7,8,9,19,11,12,13]

with ThreadPoolExecutor(max_workers=2) as executor:
    results = executor.map(print_num, numbers)

for result in results:
    print(result)
