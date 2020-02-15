""" Compute number of max overlaps given a set of time periods"""
def mininum_rooms(meetings):
    """ Function to compute max number of overlaps in the given time periods of meetings"""
    min_rooms = 0
    end_times = []
    meetings.sort(key=lambda x: (x[0], x[1]))

    for start, end in meetings:

        while end_times and end_times[0] <= start:
            end_times.pop(0)

        end_times.append(end)
        end_times.sort()

        min_rooms = max(min_rooms, len(end_times))

    return min_rooms

def main():
    """ Test cases for minimum rooms function"""
    meetings = [(1, 2), (2, 3), (5, 6), (9, 10), (2, 6)]
    print(meetings)
    print(mininum_rooms(meetings), 'rooms required')

    meetings = [(1, 2), (2, 3), (3, 4), (9, 10), (5, 6)]
    print(meetings)
    print(mininum_rooms(meetings), 'rooms required')

    meetings = [(1, 6), (2, 6), (3, 6), (4, 6), (5, 6)]
    print(meetings)
    print(mininum_rooms(meetings), 'rooms required')

    meetings = [(1, 5), (1, 5), (1, 5), (1, 5), (1, 5)]
    print(meetings)
    print(mininum_rooms(meetings), 'rooms required')

    meetings = [(1, 2), (1, 10), (2, 4), (9, 10), (3, 6)]
    print(meetings)
    print(mininum_rooms(meetings), 'rooms required')

if __name__ == '__main__':
    main()