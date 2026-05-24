"""
heapq Simple Example 2: Push Pop
Difficulty: Simple

Business Question:
Push and pop priority.

How to run:
    python simple_02_push_pop.py
"""

# ------------------------------------------------------------
# Key idea:
# This example is intentionally verbose with comments so it can be
# used as GitHub learning material and interview preparation notes.
# ------------------------------------------------------------

import heapq
h=[]; heapq.heappush(h,(2,'low')); heapq.heappush(h,(1,'high')); print(heapq.heappop(h))
