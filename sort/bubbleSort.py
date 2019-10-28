def bubbleSort(a):
	numberOfSwaps = 0
	for i in range(len(a)):
		nswaps = 0
		for j in range(len(a)-1):
			if a[j] > a[j+1]:
				temp = a[j]
				a[j] = a[j+1]
				a[j+1] = temp
				nswaps += 1
		if nswaps == 0:
			break
		numberOfSwaps += nswaps
	return numberOfSwaps

numberOfSwaps = bubbleSort(a)
print('Array is sorted in', numberOfSwaps, 'swaps.')
print('First Element:', a[0])
print('Last Element:', a[-1])