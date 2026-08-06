import threading
import time

def print_num():
    for i in range(5):
        time.sleep(1)
        print(i)
def print_num1():
    for i in range(5):
        time.sleep(1)
        print(i)
def print_num2():
    for i in range(5):
        time.sleep(1)
        print(i)
def print_num3():
    for i in range(5):
        time.sleep(1)
        print(i)
def print_num4():
    for i in range(5):
        time.sleep(1)
        print(i)
def print_num5():
    for i in range(5):
        time.sleep(1)
        print(i)
def print_num6():
    for i in range(5):
        time.sleep(1)
        print(i)

def print_let():
    for i in 'abcde':
        time.sleep(1)
        print(i)

# t = time.time()
# print_let()
# print_num()
# finalT = time.time()


# print(f'finished time {finalT - t}')


# use threads
thread = threading.Thread(target=print_num)
thread1 = threading.Thread(target=print_num1)
thread2 = threading.Thread(target=print_num2)
thread3 = threading.Thread(target=print_num3)
thread4 = threading.Thread(target=print_num4)
thread5 = threading.Thread(target=print_num5)
thread6 = threading.Thread(target=print_num6)
thread7 = threading.Thread(target=print_let)

t = time.time()
# start thread
thread.start()
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
thread6.start()
thread7.start()

# wait for thread to finish
thread.join()
thread1.join()
thread2.join()
thread3.join()
thread4.join()
thread5.join()
thread6.join()
thread7.join()

finalT = time.time()


print(f'finished time 2 {finalT - t}')