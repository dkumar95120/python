def maxArea(arr, area=0):
	if len(arr) == 0:
		return area

	min_height = min(arr)
	area = max(area, min_height*len(arr))

	idx = arr.index(min_height)

	if idx == 0:
		area = maxArea(arr[1:], area)
	elif idx == len(arr) - 1:
		area = maxArea(arr[:-1], area)
	else:
		area = maxArea(arr[idx+1:], area)
		area = maxArea(arr[:idx], area)

	return area