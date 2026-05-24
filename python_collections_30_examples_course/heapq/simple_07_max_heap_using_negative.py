"""
heapq Simple Example 7: Max Heap Using Negative
Difficulty: Simple

Business Question:
Simulate max heap.

How to run:
    python simple_07_max_heap_using_negative.py
"""

# ------------------------------------------------------------
# Key idea:
# This example is intentionally verbose with comments so it can be
# used as GitHub learning material and interview preparation notes.
# ------------------------------------------------------------

import heapq
nums=[5,1,9]; h=[-x for x in nums]; heapq.heapify(h); print(-heapq.heappop(h))
