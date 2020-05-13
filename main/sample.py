import json
import sys

# print(sys.version)
# print(sys.executable)

i = 4
d = 4.0
s = 'HackerRank '
# Declare second integer, double, and String variables.
n = 0
f = 0.0
t = ''

# Print the sum of both integer variables on a new line.
print(i + n)
# Print the sum of the double variables on a new line.
print(d + f)
# Concatenate and print the String variables on a new line
print(s + t)
# The 's' variable above should be printed first.
items = json.loads('[{"id": 1, "text": "item 1"}, {"id":2, "text": "Item 2"}]')

for item in items:
    print(item['text'])


def greeting(greeting, name):
    """Returns a greeting

    Arguments:
        greeting {string} -- greet word
        name {name} -- person's name

    Returns:
        string -- greeting for the person
    """
    return f'{greeting} {name}'


print(greeting('hello', 'world'))
