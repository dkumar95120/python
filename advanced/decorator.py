""" decorator example """

from functools import wraps
from time import time


def timer(func):
    """ Time a call to the given function

    Arguments:
        func -- function to time

    Returns:
        time -- time took to run the given function
    """
    @wraps(func)
    def f(*args, **kwargs):
        before = time()
        rv = func(*args, **kwargs)
        after = time()
        print('elapsed', after - before)
        return rv
    return f


@timer
def add(x_var=5, y_var=10):
    """ adds two numbers """
    return x_var + y_var


class Trace:
    """ Trace called function """

    def __init__(self):
        self.enabled = True

    def __call__(self, func):
        @wraps(func)
        def wrap(*args, **kwargs):
            if self.enabled:
                print('Calling {}'.format(func.__name__))
            return f(*args, **kwargs)
        return wrap


tracer = Trace()


@tracer
def rotate_list(lst):
    """ rotate given list from left """
    return lst[1:] + [lst[0]]


l = [1, 2, 3, 4]
l = rotate_list(l)
print(l)
l = rotate_list(l)
print(l)
tracer.enabled = False
l = rotate_list(l)
print(l)
l = rotate_list(l)
print(l)
