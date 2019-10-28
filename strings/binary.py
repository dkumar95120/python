def binary(n):
    s=[]
    while n:
        s.append(n%2)
        n >>= 1
    s=s[::-1]
    b = ''.join([chr(i+48) for i in s])
    return b
      
def maxOnes(n):
    sbin = binary(n)
    val = 0
    counter = 0
    for c in sbin:
        counter = counter + 1 if c == '1' else 0
        val = max(val, counter)
    return val
