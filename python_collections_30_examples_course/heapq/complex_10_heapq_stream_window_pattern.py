"""
heapq Complex Example 10: Stream Window Pattern
Difficulty: Complex

Business Question:
Solve a stream/window analytics problem using heapq concepts plus supporting collections.

How to run:
    python complex_10_heapq_stream_window_pattern.py
"""

# ------------------------------------------------------------
# Key idea:
# This example is intentionally verbose with comments so it can be
# used as GitHub learning material and interview preparation notes.
# ------------------------------------------------------------

import heapq

def solve(stream, k=3):
    # Complex heap pattern: top-K over a live stream.
    # Keep only K elements in memory, so memory is O(k).
    heap = []
    for value in stream:
        if len(heap) < k:
            heapq.heappush(heap, value)
        elif value > heap[0]:
            heapq.heapreplace(heap, value)
    return sorted(heap, reverse=True)

if __name__ == '__main__':
    print(solve([10, 50, 20, 70, 30, 90], 3))

