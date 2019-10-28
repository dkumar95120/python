# finds if the given string is a repetition of a set of characters
def isCyclic (s):
	substr = [s[0]]
	s1 = s[1:]
	for i,c in enumerate(s1) :
		if c == s[0]:
			substr.append(s[:i+1])
  
	print('substrings:', substr)
# O(n^3)
	for sub in substr:
		print('current substr:', sub)
		cyclic = True
		lsub = len(sub)
		ls = lsub
		while ls < len(s):
			next_substr = s[ls:ls+lsub]
			print('next substr:', next_substr)
			if sub != next_substr :
				cyclic = False
				break
			ls += lsub
		if cyclic:
			break
	return cyclic
