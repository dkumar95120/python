def buildCrossWordMap(crossword):
    CrossWordMap = {}
    empty ='-'
    cw_len = len(crossword)
    columns = [''.join(['+' for i in range(cw_len)]) for i in range(cw_len)]
    for i,line in enumerate(crossword):
        if empty in line:
            x = x_beg = line.find(empty)
            x_len = 1
            for ic,c in enumerate(line[x_beg+1:]):
                if c == empty:
                    if x_len == 0:
                        x = x_beg + ic + 1
                    x_len += 1
                else:
                    if x_len == 1:
                        x_len = 0
            if x_len > 1:
                direction = 0
                CrossWordMap[(i, x, direction)] = x_len

            for j,c in enumerate(line):
                if c == empty:
                    columns[j] = columns[j][:i] + empty + columns[j][i+1:]

    for j, col in enumerate(columns):
        if empty in col:
            y = y_beg = col.find(empty)
            y_len = 1
            for ic,c in enumerate(col[y_beg+1:]):
                if c == empty:
                    if y_len == 0:
                         y = y_beg + ic + 1
                    y_len += 1
                else:
                    if y_len == 1:
                        y_len = 0
            if y_len > 1:
                direction = 1
                CrossWordMap[(y, j, direction)] = y_len

    return (CrossWordMap, columns)

def crossWordPuzzle (crossword, words):
    CrossWordMap, columns = buildCrossWordMap(crossword)
    w_prop = {}
    for word in words:
        w_prop[word] = len(word)

    cw_map = sorted(CrossWordMap.items(), reverse=True, key=lambda x:x[1])
    w_map = sorted(w_prop.items(), reverse=True, key=lambda x:x[1])

    letter_map = {}
    for x,y,d in CrossWordMap.keys():
        l = CrossWordMap[(x,y,d)]
        if d == 0:
            for i,p in enumerate(range(x,x+l)):
                if (p,y) in letter_map.keys():
                    letter_map[(p,y)].append((i,d)) 
                else:
                    letter_map[(p,y)] = [(i,d)]          
        else:
            for j,p in enumerate (range(y,y+l)):
                if (x,p) in letter_map.keys():
                    letter_map[(x,p)].append((i,d))
                else:
                    letter_map [(x,p)] = [(i,d)]
        # To find common letter location with more than one frequency
        for x,y in letter_map.keys():
            if len(letter_map[(x,y)]) > 1:
                print(x,y,letter_map[(x,y)])

    cwAssigned = {}

    for w in w_map:
        # assign words based on their length to the available slot length
        for cw in cw_map:
            if cw[1] == w[1]:
                if cw[0] in cwAssigned.keys():
                    cwAssigned[cw[0]].append(w[0])
                else:
                    cwAssigned[cw[0]] = [w[0]]

    return cwAssigned





