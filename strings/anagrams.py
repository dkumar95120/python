from collections import Counter
def sherlockAndAnagrams(s):
    count = 0
    for i in range(1,len(s)+1):
        a = ["".join(sorted(s[j:j+i])) for j in range(len(s)-i+1)]
        print(a)
        b = Counter(a)
        print(b)
        for j in b:
            count+=b[j]*(b[j]-1)/2
    return int(count)

def makeAnagram(a, b):
    ctra = Counter(a)
    ctrb = Counter(b)
    n = 0
    for ch in ctra:
        if ch in ctrb:
            n += abs(ctra[ch]-ctrb[ch])
        else:
            n += ctra[ch]
    for ch in ctrb:
        if ch not in ctra:
            n += ctrb[ch]
    return n
