def min_rooms(intervals):

    starts, ends = [], []

    for s, e in intervals:
        starts.append(s)
        ends.append(e)

    starts.sort()
    ends.sort()
    print(starts)
    print(ends)

    s, e = 0, 0
    min_rooms, counter = 0, 0

    while s < len(starts):
        if starts[s] < ends[e]:
            counter += 1
            s += 1
            min_rooms = max(min_rooms, counter)
        else:
            counter -= 1
            e += 1
    return min_rooms

if __name__ == '__main__':
    meetings = [(4, 10), (1, 2), (2, 3), (3, 10), (2, 3)]
    print(meetings)
    n_rooms = min_rooms(meetings)
    print(n_rooms, "rooms required")

    meetings = [(1, 10), (1, 2), (1, 3), (1, 4), (1, 5)]
    print(meetings)
    n_rooms = min_rooms(meetings)
    print(n_rooms, "rooms required")

    meetings = [(9, 10), (1, 2), (2, 3), (3, 4), (4, 5)]
    print(meetings)
    n_rooms = min_rooms(meetings)
    print(n_rooms, "rooms required")