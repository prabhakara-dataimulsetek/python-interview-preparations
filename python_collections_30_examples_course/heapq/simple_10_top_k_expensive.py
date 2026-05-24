"""
heapq Simple Example 10: Top K Expensive
Difficulty: Simple

Business Question:
Top expensive claims.

How to run:
    python simple_10_top_k_expensive.py
"""

# ------------------------------------------------------------
# Key idea:
# This example is intentionally verbose with comments so it can be
# used as GitHub learning material and interview preparation notes.
# ------------------------------------------------------------

import heapq
claims=[100,900,300]; print(heapq.nlargest(2,claims))
