class RangeOverlap:
    def __init__(self):
        self.timeline = []

    def Add(self, start, end):
        if end > start:
            self.timeline.append((start, 'b'))
            self.timeline.append((end, 'e'))

    def MaxOverlap(self):
        n_events = len(self.timeline)
        if n_events == 0:
            return 0

        # sort start and end events in the timeline in chronological order 
        self.timeline.sort(key=lambda x:(x[0], x[1]))

        #grab first event from the timeline which must be an start event
        cur_event_time, cur_event_type = self.timeline[0]
        noverlaps = count = 1

        for i in range(1,n_events):
            next_event_time, next_event_type = self.timeline[i]
            if next_event_time > cur_event_time:
                noverlaps = max(noverlaps, count)
                # increment number of overlaps if it is an starting event otherwise decrease for the ending event
                count += 1 if next_event_type == 'b' else -1
                cur_event_time = next_event_time
            else: # event times are same therefore it is considered an overlapping event
                noverlaps = max(noverlaps, count)
                count += 1 if next_event_type == 'b' else -1

        return noverlaps