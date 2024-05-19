"""USO DE CONTEXT MANAGER Y LOCK

Podemos emplear threading.Lock junto gestores de context, es
decir con with.

La forma genral de usarlo sería:

# create a lock object
lock = threading.Lock()

# Perform some operations within a critical section
with lock:
    # lock was acquired within the with block
    # perfom operations on the shared resource
    
# the lock is released outside the with block
"""
from time import sleep
from threading import Lock, Thread
from random import randint


# gobal variable
counter: int = 0


def increase(by: int, lock: Lock):
    global counter

    with lock:
        localCounter = counter
        localCounter += by
        sleep(0.1)
        counter = localCounter
        print('counter=%d' % (counter))


def main():
    global counter

    # lock instance
    lock = Lock()

    # create threads
    thereadsToExec = [Thread(target=increase, args=(
        randint(10, 20), lock)) for _ in range(10)]

    # start and join to main thread
    [f.start() for f in thereadsToExec]
    [f.join() for f in thereadsToExec]

    # show end counter
    print('The final counter is: %d' % (counter))


if __name__ == '__main__':
    main()
