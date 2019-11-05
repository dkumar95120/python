# Generators
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

def is_palindrome(num):
    # Skip single-digit inputs
    if num // 10 == 0: return False

    temp = num
    reversed_num = 0

    while temp != 0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        temp = temp // 10

    return num if num == reversed_num else False

def getPalindrome(val):
	for i in infinite_sequence():
		if i > val:
			break
		pal = is_palindrome(i)
		if pal: print(pal)

# example of a generator expression 
def countRows(filename):
	csv_gen = (row for row in open(filename))
	row_count = 0
	for row in csv_gen:
		print(row)
		row_count += 1
	return row_count
