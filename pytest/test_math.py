def add(x, y):
    """[summary]

    Arguments:
        x {int} -- first number
        y {int} -- second number

    Returns:
        int -- sum of two numbers
    """
    return x + y


def subtract(x, y):
    """subtract y from x 

    Arguments:
        x {int} -- first number
        y {int} -- second number

    Returns:
        int -- first number - second number
    """
    return x - y


def increment(x):
    """ increment given number

    Arguments:
        x {int} -- number to be incremented

    Returns:
        int -- number + 1
    """
    return x + 1


def test_add():
    assert add(1, 2) == 3


def test_subtract():
    assert subtract(2, 1) == 1


def test_increment():
    assert increment(2) == 3
