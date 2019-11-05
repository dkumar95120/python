def queensAttack(n, k, x, y, obs):
    attacks = 0
    obstacles=set()
    for x1,y1 in obs:
        obstacles.add((x1,y1))
    obstructed=[False]*8
    for i in range(1,n):
        if y+i <= n and not obstructed[0]:
            if (x,y+i) in obstacles:
                obstructed[0] = True
            else:
                attacks += 1
        if y-i > 0 and not obstructed[1]:
            if (x,y-i) in obstacles:
                obstructed[1] = True
            else:
                attacks += 1        
        if x+i <= n and not obstructed[2]:
            if (x+i,y)  in obstacles:
                obstructed[2] = True
            else:
                attacks += 1
        if x-i > 0 and not obstructed[3]:
            if (x-i,y)  in obstacles:
                obstructed[3] = True
            else:
                attacks += 1
        if x+i <= n and y+i <= n and not obstructed[4]:
            if (x+i, y+i) in obstacles:
                obstructed[4] = True
            else:
                attacks += 1
        if x+i <= n and y-i > 0 and not obstructed[5]:
            if (x+i, y-i) in obstacles:
                obstructed[5] = True
            else:
                attacks += 1
        if x-i > 0 and y+i <= n and not obstructed[6]:
            if (x-i, y+i) in obstacles:
                obstructed[6] = True
            else:
                attacks += 1
        if x-i > 0 and y-i > 0 and not obstructed[7]:
            if (x-i, y-i) in obstacles:
                obstructed[7] = True
            else:
                attacks += 1
    return attacks
