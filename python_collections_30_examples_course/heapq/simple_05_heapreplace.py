"""
heapq Simple Example 5: Heapreplace
Difficulty: Simple

Business Question:
Replace root.

How to run:
    python simple_05_heapreplace.py
"""

# ------------------------------------------------------------
# Key idea:
# This example is intentionally verbose with comments so it can be
# used as GitHub learning material and interview preparation notes.
# ------------------------------------------------------------

import heapq
h=[1,4,6]; heapq.heapify(h); print(heapq.heapreplace(h,3), h)
