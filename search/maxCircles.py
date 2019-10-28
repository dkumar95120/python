def maxCircle(queries):
    friends = []
    groups = []
    max_friends = 2
    for a,b in queries:
        groups.append({a,b})
        group_to_join=[]
        for group in groups:
            if a in group or b in group:
                if group not in group_to_join:
                    group_to_join.append(group)
        if len(group_to_join) > 1:
            groupa = group_to_join[0]
            groups.remove(groupa)
            for i in range(1,len(group_to_join)):
                groupa = groupa.union(group_to_join[i])
                groups.remove(group_to_join[i])
            max_friends = max(max_friends, len(groupa))
            groups.append(groupa)            
        friends.append(max_friends)
    return friends