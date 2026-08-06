from concurrent.futures import ProcessPoolExecutor
import time

def square_num(number):
    time.sleep(2)
    return number**2

numbers = [1,2,3,4,5,6,7,8,9,19,11,12,13]
if __name__ == '__main__': 
    with ProcessPoolExecutor(max_workers=4) as executor:
        results = executor.map(square_num, numbers)

    print(results)

    for result in results:
        print(result)
