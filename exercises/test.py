import os


def my_print(*args):
    for item in args:
        print(item)


def main():
    msg = 'Hello world!'
    question = "How are you?"
    my_print(msg, question)
    print(msg, question)


if __name__ == "__main__":
    main()
