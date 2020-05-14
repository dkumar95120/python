""" compute factorial """
from functools import reduce


def factorial(num):
    """ compute factorial using reduce """
    return reduce((lambda x, y: x*y), range(1, num + 1))


def main():
    """ Driver for testing factorial function """
    for num in range(1, 10):
        print(num, factorial(num))
    print("The End")


if __name__ == '__main__':
    main()
