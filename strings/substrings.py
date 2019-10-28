def makeSubstrings(s):
    ls = len(s)
    substr=[]
    for l in range(1,ls+1):
        for i in range(ls+1-l):
            substr.append(s[i:i+l])
    return substr
def isSpecialString(s):
    ctr = Counter(s)
    if len(ctr) > 2:
        return 0
    freq = sorted(ctr.items(), key=lambda x:x[1])
    if freq[0][1] > 1:
        return 0
    elif s.index(freq[0][0]) != len(s) >> 1:
        return 0
    else:
        return 1
    
def substrCount(n, s):
    ctr = Counter(s)
    # special case if there is just one letter type in the string
    if len(ctr) == 1:
        for c in ctr:
            n = ctr[c]*(ctr[c]+1)/2
        return int(n)
    # since all individual characters qualify to be a special string initialize n with the length of the string
    n = len(s)
    # now make substrings of odd lengths per the special string requirement
    substrs = makeSubstrings(s)
    for sub in substrs:
        n += isSpecialString(sub)

    return n


def substrCount(n, s):
    tot = 0
    count_sequence = 0
    prev = ''
    for i,v in enumerate(s):
        # first increase counter for all seperate characters
        count_sequence += 1
        if i and (prev != v):
            # if it is not the first char in the string and it is not same as previous char,
            # check for sequence x.x, xx.xx, xxx.xxx with condition s[i-j] == prev == s[i+j]
            # and we know it cant be longer on the right side than
            # the sequence we already found on the left side or j <= count_sequence
            j = 1
            while ((i-j) >= 0) and ((i+j) < len(s)) and j <= count_sequence:
                # make sure the chars to the right and left are equal
                # to the char in the previous found squence
                if s[i-j] == prev == s[i+j]:
                    # if so increase total score and step one step further out
                    tot += 1
                    j += 1
                else:
                    # no need to loop any further if this loop did 
                    # not find an x.x  pattern
                    break
            #if the current char is different from previous, reset counter to 1
            count_sequence = 1  
        tot += count_sequence            
        prev = v
    return tot    

def isSorted(a):
    i = 1
    while i < len(a) and a[i] > a[i-1]:
        i += 1
    return i == len(a)  

def commonStr(s1, s2):
    # special case
    if s1 == s2:
        return len(s)
    order2 = []
    common1 = 0
    comstr1 = ''
    ls1=list(s1)
    ls2=list(s2)
    for i,c in enumerate(ls1):
        while c in ls2:
            j = ls2.index(c)
            order2.append(j)
            if isSorted(order2):
                common1 += 1
                comstr1 += c
                ls2[j]='0'
                break
            else:
                order2.pop()
                ls2[j]='0'
    common2 = 0
    ls2=list(s2)
    order1 = []
    comstr2 = ''
    for i,c in enumerate(ls2):
        while c in ls1:
            j = ls1.index(c)
            order1.append(j)
            if isSorted(order1):
                common2 += 1
                comstr2 += c
                ls1[j]='0'
                break
            else:
                order1.pop()
                ls1[j]='0'   
    
    return comstr1 if common1 > common2 else comstr2