""" script to solicit user input """
if __name__ == '__main__':
    n = int(input())
    phone_book = {}
    for i in range(n):
        name, number = input().rstrip().split()
        phone_book[name] = number

    for i in range(n):
        name = input().rstrip()
        if name in phone_book.keys():
            print('{0}={1}'.format(name, phone_book[name]))
        else:
            print('Not found')
