from itertools import product
lookup = {
'1':['a','b','c'],
'2':['d','e','f'],
'3':['g','h','i'],
'4':['j','k','l'],
'5':['m','n','o'],
'6':['p','q','r'],
'7':['s','t','v'],
'8':['w','x','y'],
'9':['z','%','-'],
'0':['*','+','#']}

def phoneNumberCombs(numstr):
	possibilities = [lookup[x] for x in numstr]
	return [''.join(x) for x in product(*possibilities) if x]