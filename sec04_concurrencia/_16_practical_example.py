from threading import Thread, Event
from urllib import request


def downloadFile(url: str, event: Event):
    print('Downloading file from %s...' % (url))
    _ = request.urlretrieve(url, 'rfc793.txt')
    event.set()


def processFile(event: Event):
    print('Waiting for the file to be downloaded. . . ')
    event.wait()
    print('File download completed. Starting file processing. . . ')

    # count the number of words in the file
    wordCount = 0
    with open(file='rfc793.txt', mode='r') as file:
        for line in file:
            words = line.split()
            wordCount += len(words)

    # show results
    print('Number of words in the file: %d' % (wordCount))


def main():
    # create event instance
    event = Event()

    # create the file download thread
    downloadThread = Thread(
        target=downloadFile,
        args=(
            'https://www.ietf.org/rfc/rfc793.txt',
            event
        ),
    )

    # start file downdload thread
    downloadThread.start()

    # create and start file processong thread
    processThread = Thread(target=processFile, args=(event, ))
    processThread.start()

    # wait for both threads to complete
    downloadThread.join()
    processThread.join()

    # end message
    print('Main thread finished. . . ')


if __name__ == '__main__':
    main()
