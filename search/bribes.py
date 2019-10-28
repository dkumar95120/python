# Complete the minimumBribes function below.
def minimumBribes(q):
    moves = 0
    for i,v in enumerate(q):
        if v - i > 3:
            print("Too chaotic")
            return
        # find people with higher queue number ahead of this person v
        for j in range(i):
            if q[j] > v:
                moves += 1
    print(moves)
    return 