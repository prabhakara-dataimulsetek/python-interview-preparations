from collections import defaultdict, deque

def rate_limit(events, limit, window):
    buckets = defaultdict(deque)
    decisions = []
    for user, ts in events:
        q = buckets[user]
        while q and q[0] <= ts - window:
            q.popleft()
        if len(q) < limit:
            q.append(ts)
            decisions.append(True)
        else:
            decisions.append(False)
    return decisions
