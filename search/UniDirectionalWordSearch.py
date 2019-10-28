def wordSearch (x, y, dx, dy, index, word, board):
    w = len(board[0])
    h = len(board)
    # return if have hit the wall
    if x < 0 or x >= w or y < 0 or y >= h:
        return 0
    if board[x][y] != word[index]:
        return 0
    else:
        if index == len(word) - 1:
            return 1
        else:
            return wordSearch (x+dx, y+dy, dx, dy, index+1, word, board)

def findWord (board, word):
    count = 0
    for x,row in enumerate(board):
        for y,ch in enumerate(row):
            if board[x][y] == word[0]:
                for dx in (-1, 0, 1):
                    for dy in (-1,0,1):
                        if dx != 0 or dy != 0:
                            count += wordSearch (x+dx, y+dy, dx, dy, 1, word, board)

    return count


word='LOG'
board=['ALOG','QOLR','TGCT','IEAL']
import pdb; pdb.set_trace()
print(findWord(board, word))