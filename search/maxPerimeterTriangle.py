def isValidTriangle(s):
	s.sort()
	if (s[0] + s[1]) > s[2]:
		return True
	else:
		return False

def maxPerimeterTriangle(s):
	s.sort(reverse=True)
	i = 0
	t = []
	ns = len(s)
	while True:
		# exit if no valid triangle can be formed
		if (i+2) >= ns:
			break
		triad = [s[i], s[i+1], s[i+2]]
		if isValidTriangle (triad) :
			t = triad
			break
		else:
			i += 1

	if bool(t):
		return sorted(t)
	else:
		return [-1]

