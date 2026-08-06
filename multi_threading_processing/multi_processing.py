import multiprocessing
import time

def square_num():
    for i in range(5):
        time.sleep(1)
        print(i**2)

def cube_num():
    for i in range(5):
        time.sleep(1.5)
        print(i**3)

if __name__ == '__main__': 
    t = time.time()

    # create 2 processes
    p1 = multiprocessing.Process(target=square_num)
    p2 = multiprocessing.Process(target=cube_num)

    # start processes
    p1.start()
    p2.start()

    # wait for processes to finish
    p1.join()
    p2.join()

    finalT = time.time()

    print(f'finished time {finalT - t}')