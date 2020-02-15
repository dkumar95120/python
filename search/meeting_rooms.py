""" Calculates number of meeting rooms"""
def minimum_rooms(meetings):
    """ Calculates number of minimum rooms required for a given set of meetings """
    nrooms = 0
    room_stack = []
    meetings.sort(key=lambda x: (x[0], x[1]))

    for start, end in meetings:
        while room_stack and room_stack[0] <= start:
            room_stack.pop(0)
        room_stack.append(end)
        room_stack.sort()

        nrooms = max(nrooms, len(room_stack))

    return nrooms

def meeting_rooms(time_periods):
    """ Returns number of rooms required for the given meetings time_periods"""
    # build a timeline from the time_periods provided
    timeline = []
    for t_start, t_end in time_periods:
        timeline.append((t_start, 's'))
        timeline.append((t_end, 'e'))

    # sort events in timeline in chronological order of the meeting start and end time
    timeline.sort(key=lambda x: x[0])
    n_events = len(timeline)

    #grab first event from the timeline which must be an start event
    cur_event_time, _ = timeline[0]
    nrooms = count = 1

    for i in range(1, n_events):

        next_event_time, next_event_type = timeline[i]

        if next_event_time > cur_event_time:
            nrooms = max(nrooms, count)
            count += 1 if next_event_type == 's' else -1
            cur_event_time = next_event_time
        else:
            count += 1 if next_event_type == 's' else -1

    return nrooms

def main():
    """ Driver program to test minimum room functions """
    print("Enter number of meetings")
    n_meetings = int(input().rstrip())

    meetings = []
    print("Enter start and end times as int for each meeting")
    for _ in range(n_meetings):
        start, end = map(int, input().rstrip().split())
        meetings.append((start, end))

    print(f'{minimum_rooms(meetings)} minimum rooms are required')
    print(f'{meeting_rooms(meetings)} meeting rooms are required')

if __name__ == '__main__':
    main()
