"""
collections.Counter Complex Example 1: Stream Window Pattern
Difficulty: Complex

Business Question:
Solve a stream/window analytics problem using collections.Counter concepts plus supporting collections.

How to run:
    python complex_01_counter_stream_window_pattern.py
"""

# ------------------------------------------------------------
# Key idea:
# This example is intentionally verbose with comments so it can be
# used as GitHub learning material and interview preparation notes.
# ------------------------------------------------------------

def solve(events, window_size=3):
    # Complex pattern: sliding window + frequency map + ranking.
    # This is common in HackerRank-style stream analytics problems.
    from collections import Counter, deque
    window = deque()
    freq = Counter()
    answer = []
    for event in events:
        window.append(event)
        freq[event] += 1
        if len(window) > window_size:
            old = window.popleft()
            freq[old] -= 1
            if freq[old] == 0:
                del freq[old]
        # Pick most frequent event in current window; tie breaks alphabetically.
        best = sorted(freq.items(), key=lambda item: (-item[1], item[0]))[0]
        answer.append(best)
    return answer

if __name__ == '__main__':
    print(solve(['claim','benefit','claim','card','benefit','benefit'], 3))

