""" function to compute min overlaps for given time periods """
def minimum_rooms(intervals):
    """ function to compute min rooms required for given time intervals """
    starts, ends = [], []

    for start, end in intervals:
        starts.append(start)
        ends.append(end)

    starts.sort()
    ends.sort()

    beg, end = 0, 0
    min_rooms, counter = 0, 0

    while beg < len(starts):
        if starts[beg] < ends[end]:
            counter += 1
            beg += 1
            min_rooms = max(min_rooms, counter)
        else:
            counter -= 1
            end += 1

    return min_rooms

def main():
    """ driver for testing min_rooms function """
    meetings = [(4, 10), (1, 2), (2, 3), (3, 10), (2, 3)]
    print(meetings)
    print(minimum_rooms(meetings), "rooms required")

    meetings = [(1, 10), (1, 2), (1, 3), (1, 4), (1, 5)]
    print(meetings)
    print(minimum_rooms(meetings), "rooms required")

    meetings = [(9, 10), (1, 2), (2, 3), (3, 4), (4, 5)]
    print(meetings)
    print(minimum_rooms(meetings), "rooms required")

if __name__ == '__main__':
    main()
