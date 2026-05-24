"""
heapq Simple Example 1: Min Heap Basic
Difficulty: Simple

Business Question:
Get smallest item.

How to run:
    python simple_01_min_heap_basic.py
"""

# ------------------------------------------------------------
# Key idea:
# This example is intentionally verbose with comments so it can be
# used as GitHub learning material and interview preparation notes.
# ------------------------------------------------------------

import heapq
h=[5,1,3]; heapq.heapify(h); print(heapq.heappop(h))
