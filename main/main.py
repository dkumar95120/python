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

i = 4
d = 4.0
s = 'HackerRank '
# Declare second integer, double, and String variables.
n = 0
f = 0.0
t = ''

# Read and save an integer, double, and String to your variables.
n = int(input().rstrip())
f = float(input().rstrip())
t = input().rstrip()


# Print the sum of both integer variables on a new line.
print(i + n)
# Print the sum of the double variables on a new line.
print(d + f)
# Concatenate and print the String variables on a new line
print(s + t)
# The 's' variable above should be printed first.
