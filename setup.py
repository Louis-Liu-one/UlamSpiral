
from setuptools import setup, Extension


def main():
    ext = Extension(
        'eratothenes',
        ['eratothenes.c'])
    setup(
        name='eratothenes',
        ext_modules=[ext])


if __name__ == '__main__':
    main()
