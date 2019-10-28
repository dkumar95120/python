def getMatchedWordComb(L, index, substr, words):
	while word in words:
		lw = len(word)
		ls = len(substr)
		if len(word) > len(substr):
			continue
		if word == substr[-lw:]:
			L[index] += L[ls-lw]
	return

def getMatchedWordComb(s, words):
	L = [0 for i in range(len(s) + 1)]
	L[0] = 1
	for i,c in enumerate(s):
		getMatchedWordComb(L, i+1,s[:i], words)

	print(L)
	return L[-1]
