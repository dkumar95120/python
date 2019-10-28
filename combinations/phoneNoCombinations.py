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

def buildCombinations(phoneNo, comb, index, bank):
# Terminating conditions
	if index == len(phoneNo):
		bank.append(comb)
		return

	for i in range(3):
		comb1 = comb + lookup[phoneNo[index]][i]
		buildCombinations(phoneNo, comb1, index+1, bank)

def getCombinations(phoneNo):
	index = 0
	bank = []
	buildCombinations(phoneNo,'',index, bank)
	print(bank)
	return
	