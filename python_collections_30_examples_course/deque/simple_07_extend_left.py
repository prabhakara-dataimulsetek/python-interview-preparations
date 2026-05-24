"""
collections.deque Simple Example 7: Extend Left
Difficulty: Simple

Business Question:
Extend left reverses input order.

How to run:
    python simple_07_extend_left.py
"""

# ------------------------------------------------------------
# Key idea:
# This example is intentionally verbose with comments so it can be
# used as GitHub learning material and interview preparation notes.
# ------------------------------------------------------------

from collections import deque
d=deque([3]); d.extendleft([1,2]); print(d)
