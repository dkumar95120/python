def countTriplets(arr, r):
    ctr = Counter(arr)
    if r == 1:
        triplets = 0
        for i in ctr.keys():
            n = ctr[i]
            if i > 0 and n > 2:
                triplets += n*(n-1)*(n-2)/6
        return int(triplets)
    # build a hash map of values and their respective indices
    ctr = {}
    for i,v in enumerate(arr):
        if v in ctr:
            ctr[v].append(i)
        else:
            ctr[v] = [i]
    # sort all indices for each value in ascending order
    for v in ctr:
        ctr[v].sort()
        print(v, ctr[v])

    triplets = 0
    for i,v in enumerate(arr):
        if v*r in ctr and v*r*r in ctr:
            for j in ctr[v*r]:
                if j < i:
                    continue
                else:
                    for k in ctr[v*r*r]:
                        if k > j:
                            break
                    if k > j:
                        p = ctr[v*r*r].index(k)
                        triplets += len(ctr[v*r*r]) - p
    return triplets