""" example of a context manager """
import os
from sqlite3 import connect
from contextlib import contextmanager


def readfile(file):
    """ read given file """
    if not os.path.isfile(file):
        print(file, 'does not exist')
        return
    with open(file, 'r') as fptr:
        for line in fptr:
            print(line)


@contextmanager
def temptable(cur):
    """ get create a row in the given table """
    cur.execute('create table points(x int, y int)')
    try:
        yield
    finally:
        cur.execute('drop table points')


def main():
    """ Driver for temptable """
    with connect('test.db') as test_db:
        cur = test_db.cursor()
        with temptable(cur):
            cur.execute('insert into points (x,y) values (1,1)')
            cur.execute('insert into points (x,y) values (1,2)')
            cur.execute('insert into points (x,y) values (2,1)')
            for row in cur.execute('select x, y from points'):
                print(row)
            for row in cur.execute('select sum(x * y) from points'):
                print(row)


if __name__ == '__main__':
    main()
