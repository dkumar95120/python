# Complete the superDigit function below.
def sumOfDigits (digits):
    total = 0
    for c in digits:
        total += ord(c) - ord('0')
    return total

def superDigit(n,k):
    print(n,k)
    if (int(n) < 10) and (k == 1):
        return int(n)
    total = k*sumOfDigits(n)
    n = superDigit(str(total),1)
    return n
