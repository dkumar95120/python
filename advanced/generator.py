""" example of generator function """


# Generators
def infinite_sequence():
    """ yield next number """
    num = 0
    while True:
        yield num
        num += 1


def is_palindrome(num):
    """ is given number a palindrome """
    # Skip single-digit inputs
    if num // 10 == 0:
        return False

    temp = num
    reversed_num = 0

    while temp != 0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        temp = temp // 10

    return num if num == reversed_num else False


def get_palindrome(val):
    """ print palindrome numbers in the given range """
    for i in infinite_sequence():
        if i > val:
            break
        pal = is_palindrome(i)
        if pal:
            print(pal)

# example of a generator expression


def main():
    """ Driver for palindrome function """
    get_palindrome(200)


if __name__ == "__main__":
    main()
