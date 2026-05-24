"""
heapq Medium Example 1: Aggregation Pattern
Difficulty: Medium

Business Question:
Use heapq to solve an aggregation/ranking business problem.

How to run:
    python medium_01_heapq_aggregation_pattern.py
"""

# ------------------------------------------------------------
# Key idea:
# This example is intentionally verbose with comments so it can be
# used as GitHub learning material and interview preparation notes.
# ------------------------------------------------------------

import heapq

def solve(records, k=3):
    # Medium heap pattern: keep top K values without sorting all rows.
    heap = []
    for key, value in records:
        heapq.heappush(heap, (value, key))
        if len(heap) > k:
            heapq.heappop(heap)
    return sorted(heap, reverse=True)

if __name__ == '__main__':
    print(solve([('A',10),('B',5),('C',20),('D',7)], 2))

