from threading import Thread, Lock
import time

tLock = Lock()

def timer(name, delay, repeat):
    print(f'Timer: {name} started')
    tLock.acquire()
    print(f'Timer: {name} has acquired the lock')
    while repeat > 0:
        time.sleep(delay)
        print(f"{name}: {time.ctime(time.time())}")
        repeat -= 1
    tLock.release()
    print(f'Timer: {name} has released the lock')
    print(f'Timer: {name} completed')

def Main():
    t1 = Thread(target=timer, args=("Timer1", 1, 5))
    t2 = Thread(target=timer, args=("Timer2", 2, 5))
    t1.start()
    t2.start()

    print("Main completed")

if __name__ == '__main__':
    Main()

