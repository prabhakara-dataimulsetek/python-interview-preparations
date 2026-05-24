"""
heapq Simple Example 6: Heappushpop
Difficulty: Simple

Business Question:
Push then pop smallest.

How to run:
    python simple_06_heappushpop.py
"""

# ------------------------------------------------------------
# Key idea:
# This example is intentionally verbose with comments so it can be
# used as GitHub learning material and interview preparation notes.
# ------------------------------------------------------------

import heapq
h=[2,4]; heapq.heapify(h); print(heapq.heappushpop(h,1), h)
