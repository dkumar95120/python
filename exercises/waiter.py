#!/bin/python3

import os
import sys
from collections import defaultdict

#
# Complete the waiter function below.
#
def prime_numbers(n):
    # initial prime number list
    prime_list = [2]
    # first number to test if prime
    num = 3
    # keep generating primes until we get to the nth one
    while len(prime_list) < n:

        # check if num is divisible by any prime before it
        for p in prime_list:
            # if there is no remainder dividing the number
            # then the number is not a prime
            if num % p == 0:
                # break to stop testing more numbers, we know it's not a prime
                break

        # if it is a prime, then add it to the list
        # after a for loop, else runs if the "break" command has not been given
        else:
            # append to prime list
            prime_list.append(num)

        # same optimization you had, don't check even numbers
        num += 2

    # return the last prime number generated
    return prime_list

def waiter(number, q):
    #
    # Write your code here.
    #
    a = defaultdict(list)
    b = defaultdict(list)
    primes = prime_numbers(q)
    a[0] = number
    result = []
    for i in range(1,q+1):
        if not bool(a[i-1]):
            break


        while a[i-1]:
            k = a[i-1].pop()
            if k % primes[i-1]:
                a[i].append(k)
            else:
                b[i].append(k)

        result.extend(b[i][::-1])

    result.extend(a[q][::-1])
    return result

if __name__ == '__main__':

    print("Enter number of plates and iterations")

    nq = input().split()

    n = int(nq[0])

    q = int(nq[1])

    print("Enter number on each plate")

    number = list(map(int, input().rstrip().split()))

    result = waiter(number, q)

    print('\n'.join(map(str, result)))
