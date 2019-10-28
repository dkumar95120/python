def removeExtraLowercaseLetters (la,lb):
    for i in range(len(lb)):
        while (i < len(la)) and (la[i].upper() != lb[i]):
            if (i < len(la)) and (la[i] >= 'a'):
                del la[i]
            else:
                break
        while (i < len(la)-1) and (la[i+1].upper() == lb[i]):
            if (i < len(la)) and (la[i] >= 'a'):
                del la[i]
            else:
                break

    return la

def abbreviation(a, b):
    if len(b) > len(a):
        return 'NO'

    la = list(a)
    lb = list(b)
    la = removeExtraLowercaseLetters(la,lb)

    la.reverse()
    lb.reverse()
    la = removeExtraLowercaseLetters(la,lb)

    la.reverse()

# strip trailing lowercase letters
    while len(la) > len(lb) and la[-1] >= 'a':
        del la[-1]

    x = ''.join(la)
    print(len(x),x)
    print(len(b),b)
    if x.upper() == b:
        return 'YES'
    else:
        return 'NO'
