"""THREADPOOLEXECUTOR EXAMPLE


"""
from concurrent.futures import ThreadPoolExecutor
from urllib.request import urlopen
import time
import os


def downloadImage(url: str) -> None:
    imageData = None
    with urlopen(url) as f:
        imageData = f.read()

    if not imageData:
        raise Exception('Error: could not download the image from %s.' % (url))

    # cer
    filename = os.path.basename(url)
    with open(filename, mode='wb') as imageFile:
        imageFile.write(imageData)
        print('%s was downloaded . . . ' % (filename))


if __name__ == '__main__':

    # init time counter
    ti = time.perf_counter()

    urls = [
        'https://upload.wikimedia.org/wikipedia/commons/9/9d/Python_bivittatus_1701.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/4/48/Python_Regius.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/d/d3/Baby_carpet_python_caudal_luring.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/f/f0/Rock_python_pratik.JPG',
        'https://upload.wikimedia.org/wikipedia/commons/0/07/Dulip_Wilpattu_Python1.jpg',
    ]

    with ThreadPoolExecutor as executor:
        executor
