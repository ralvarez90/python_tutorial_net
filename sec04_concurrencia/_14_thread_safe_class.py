"""CREANDO CLASE THREAD SAFE USANDO LOCK
"""
from threading import Thread, Lock
from time import sleep


class Counter:
    def __init__(self) -> None:
        self.value = 0
        self.lock = Lock()

    def increase(self, by: int):
        with self.lock:
            currentValue = self.value
            currentValue += by
            sleep(0.1)
            self.value = currentValue
            print('counter=%d' % (self.value))


def main():

    # counter instance
    counter = Counter()

    # create threads
    t1 = Thread(target=counter.increase, args=(10, ))
    t2 = Thread(target=counter.increase, args=(20, ))

    # starts and join to main thread
    t1.start() or t1.join()
    t2.start() or t2.join()

    # shoe end message
    print('The final counter is: %d' % (counter.value))


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . . ')
