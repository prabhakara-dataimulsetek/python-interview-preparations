"""
heapq Simple Example 9: Priority With Tie
Difficulty: Simple

Business Question:
Use tuple priority and tie-breaker.

How to run:
    python simple_09_priority_with_tie.py
"""

# ------------------------------------------------------------
# Key idea:
# This example is intentionally verbose with comments so it can be
# used as GitHub learning material and interview preparation notes.
# ------------------------------------------------------------

import heapq
h=[]; heapq.heappush(h,(1,0,'A')); heapq.heappush(h,(1,1,'B')); print(heapq.heappop(h))
