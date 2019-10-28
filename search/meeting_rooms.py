def meeting_rooms (time_periods):
	# build a timeline from the time_periods provided
	timeline = []
	for t_start, t_end in time_periods:
		timeline.append((t_start, 's'))
		timeline.append((t_end, 'e'))

	# sort events in timeline in chronological order 
	timeline.sort(key=lambda x:x[0])
	n_events = len(timeline)

	#grab first event from the timeline which must be an start event
	cur_event_time, cur_event_type = timeline[0]
	nrooms = count = 1

	for i in range(1,n_events):

		next_event_time, next_event_type = timeline[i]

		if next_event_time > cur_event_time:
			nrooms = max(nrooms, count)
			count += 1 if next_event_type == 's' else -1
			cur_event_time = next_event_time
		else:
			count += 1 if next_event_type == 's' else -1

	return nrooms

