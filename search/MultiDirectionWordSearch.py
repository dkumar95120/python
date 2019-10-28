def wordSearch (x,y, index, visited, word, board):
	w = len(board[0])
	h = len(board)
	# return if have hit the wall
	if x < 0 or x > w or y < 0 or y > h:
		return 0
	if board[x][y] != word[index]:
		return 0
	else:
		if index == len(word) - 1:
			return 1
		else:
			count = 0
			for dx in (-1, 0, 1):
				for dy in (-1, 0, 1):
					if dx != 0 or dy != 0:
						# depth first search in each of the following directions
						# starting top-left, top, top-right, left, right, ... 
						if (x+dx, y+dy) not in visited:
							visited.add((x+dx,y+dy))
							count += wordSearch (x+dx,y+dx, index+1, visited, word, board)
			return count

def findWord (board, word):
	for x,row enumerate(board):
		for y,ch in enumerate(row):
			visited = set([(x,y)])
			count += wordSearch (x,y, 0, visited, word, board)

    return count



