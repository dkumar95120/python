def isCyclic(s):
	fst_ptr = 0
	sec_ptr = 1
	slen = len(s)

	while sec_ptr < slen:
		print(fst_ptr, sec_ptr)
		if s[fst_ptr] == s[sec_ptr]:
			fst_ptr += 1
			sec_ptr += 1
		else:
			fst_ptr = 0
			if s[fst_ptr] != s[sec_ptr]:
				sec_ptr += 1

		sub_len = sec_ptr - fst_ptr

	print(s[:sub_len])

# Substring length cannot be more that half of the overall string length
	if sub_len > slen/2:
		return False
	else:
		return s[:sub_len] == s[-sub_len:]
