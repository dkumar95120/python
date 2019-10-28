def doStringsMatch(L,r,c,a,b):
    # first check if top-left i.e. substring a and b thus barring the 
    # current letters are matching, and
    # the current letters match (optionally capitalizing letter in a)

    return (r > 0 and c > 0 and L[r-1][c-1] and a[c-1].upper() == b[r-1]) or \
           (c > 0 and L[r][c-1] and a[c-1] >= 'a')

def prettyPrint(L):
    for i in range(len(L)):
        print(L[i])
    print()

def abbreviation(a,b):
    L = [[False for i in range(len(a)+1)] for j in range(len(b)+1)]
    # empty strings match
    L[0][0] = True
    for r in range(len(L)):
        for c in range(len(L[0])):
            if r+c > 0:
                L[r][c] = doStringsMatch (L, r, c, a, b)
        prettyPrint(L)
    return L[len(b)][len(a)]

a='AbcDE'
b='ABDE'

print(abbreviation(a,b))