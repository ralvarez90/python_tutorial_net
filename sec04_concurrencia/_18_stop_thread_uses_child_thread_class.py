"""STOPPING A THREAD THAT USES A CHILD OF THE THREAD CLASS
"""
from threading import Thread, Event
from time import sleep


class Worker(Thread):
    def __init__(self, event: Event, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.event = Event()

    def run(self) -> None:
        for i in range(6):
            print('Running #%d' % (i+1))
            sleep(1)
            if self.event.is_set():
                print('The thread was stopped prematurely.')
                break
        else:
            print('The thread was stopped maturely.')


def main():

    # create event
    event = Event()

    # create a new worker thread
    thread = Worker(event)
    thread.start()

    # suspend the thread after 3 seconds
    sleep(3)

    # stop the child process.
    event.set()


if __name__ == '__main__':
    main()
