def min_meeting_rooms(intervals):
    events = []
    for s, e in intervals:
        events.append((s, 1))
        events.append((e, -1))
    events.sort(key=lambda x: (x[0], x[1]))
    cur = ans = 0
    for _, delta in events:
        cur += delta
        ans = max(ans, cur)
    return ans
