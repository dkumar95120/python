import argparse


def fib(num):
    a, b = 0, 1
    for _ in range(num):
        a, b = b, a + b
    return a


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'num', help='The fibonacci number you wish to calculate.', type=int)
    parser.add_argument(
        '-o', '--output', help='Output result to a file.', action='store_true')

    group = parser.add_mutually_exclusive_group()
    group.add_argument('-v', '--verbose', action='store_true')
    group.add_argument('-q', '--quiet', action="store_true")

    args = parser.parse_args()
    result = fib(args.num)

    output = f'The {args.num}th fib number is {result}'
    if args.verbose:
        print(output)
    elif args.quiet:
        print(result)
    else:
        print(f'fib({args.num}) = {result}')

    if args.output:
        with open("fibonacci.txt", 'a') as fptr:
            fptr.write(f'{output}\n')


if __name__ == '__main__':
    main()
