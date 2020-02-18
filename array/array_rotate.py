def main():
    """ driver to test array rotation """
    print("Enter number of rotation")
    nrot = int(input().rstrip())
    print("Enter array values")
    arr = list(map(int, input().rstrip().split()))
    for _ in range(nrot):
        arr.insert(0, arr.pop())
    print(arr)

if __name__ == '__main__':
    main()
