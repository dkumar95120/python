#!/bin/python3
''' Hackerrank question of finding frequency of numbers in a given dictionary'''
from collections import defaultdict
# Complete the freqQuery function below.


def freq_query(queries):
    ''' find frequecy of numbers in the given list'''
    answer = []
    numbers = defaultdict(int)
    freq = defaultdict(int)
    for ops, val in queries:
        if ops == 1:
            freq[numbers[val]] = max(0, freq[numbers[val]] - 1)
            numbers[val] += 1
            freq[numbers[val]] += 1
        elif ops == 2:
            freq[numbers[val]] = max(0, freq[numbers[val]] - 1)
            numbers[val] = max(0, numbers[val] - 1)
            if numbers[val] > 0:
                freq[numbers[val]] += 1
        elif ops == 3:
            answer.append(1 if freq[val] > 0 else 0)

    return answer


def main():
    ''' driver function '''
    print
    n_query = int(input('Number of queries\n').strip())

    queries = []
    print('Queries')

    for _ in range(n_query):
        queries.append(list(map(int, input().rstrip().split())))

    print('Answer')
    print('\n'.join(map(str, freq_query(queries))))


if __name__ == '__main__':
    main()
