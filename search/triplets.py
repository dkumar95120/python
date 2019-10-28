from collections import Counter
def triplets(a, b, c):
    a = list(sorted(set(a)))
    b = list(sorted(set(b)))
    c = list(sorted(set(c)))
    
    ai = 0
    bi = 0
    ci = 0
    
    ans = 0
    
    while bi < len(b):
        while ai < len(a) and a[ai] <= b[bi]:
            ai += 1
        
        while ci < len(c) and c[ci] <= b[bi]:
            ci += 1
        
        ans += ai * ci
        bi += 1
    
    return ans

# find triplets of geometric sequence which i < j < k
from collections import defaultdict
def countTriplets(arr, r):
    firstNumHist = defaultdict(int)
    secondNumHist = defaultdict(int)
    triplets = 0
    for val in arr:
        if val % r == 0:
            # if there is a valid predecessor in the geo sequence,
            # (aka the current value is divisible by r) then calculate it
            predecessor = int(val/r)
            # each time we noted the predecessor as a valid 2nd element
            # in the geo sequence over r, we can now consider the
            # current val as a valid 3rd element in the geo sequence,
            # thereby creating a triplet
            triplets += secondNumHist[predecessor]
            # each time we noted the predecessor as a valid 1st element
            # in the geo sequence over r, we can now consider the
            # current val as a valid 2nd element in the geo sequence
            secondNumHist[val] += firstNumHist[predecessor]
        # it is valid for every number to be the first number in a
        # geometric sequence over r
        firstNumHist[val] += 1
    return triplets

fptr = open('triplets.dat', 'r')
n, r = map(int, fptr.readline().rstrip().split())
arr = list(map(int, fptr.read().rstrip().split()))

print(countTriplets(arr, r))
