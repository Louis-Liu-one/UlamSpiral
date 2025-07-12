
from PIL import Image
import time

from eratothenes import *


class Eratothenes:

    def __init__(self, size):
        self._isprime = [True] * size
        self._isprime[0] = False
        self._num = 0
        self._size = size

    def __iter__(self):
        return self

    def __next__(self):
        self._num += 1
        if self._num > self._size:
            raise StopIteration
        if self._isprime[self._num - 1]:
            for comp in range(self._num, self._size + 1, self._num):
                self._isprime[comp - 1] = False
            self._isprime[self._num - 1] = True
        return self._num, self._isprime[self._num - 1]


def fill_image(img, color):
    x, y = img.width // 2 - 1, img.height // 2
    dx, dy = (0, 1, 0, -1), (-1, 0, 1, 0)
    heading, forward, nowforward = 0, 1, 1
    nowhx, nowhy = dx[heading], dy[heading]
    eratothenes_begin(img.width * img.height)
    while True:
        retval = eratothenes_next()
        if retval is None:
            break
        num, is_prime = retval
        if is_prime:
            img.putpixel((x, y), color)
        x += nowhx
        y += nowhy
        nowforward -= 1
        if nowforward == 0:
            heading = (heading + 1) % 4
            nowhx, nowhy = dx[heading], dy[heading]
            if heading in (0, 2):
                forward += 1
                print(
                    '\r' + str(round(num / img.width / img.height * 100, 2))
                    + '% ' + str(num), end='')
            nowforward = forward
    eratothenes_end()


if __name__ == '__main__':
    t = time.time()
    w, h = 16384, 16384
    img = Image.new('RGB', (w, h), (255, 255, 255))
    fill_image(img, (0, 0, 0))
    img.save('UlamSpiral.png')
    img.close()
    print('\nTime: ', time.time() - t, 's', sep='')
