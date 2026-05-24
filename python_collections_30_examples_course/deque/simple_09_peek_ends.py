"""
collections.deque Simple Example 9: Peek Ends
Difficulty: Simple

Business Question:
Peek both ends.

How to run:
    python simple_09_peek_ends.py
"""

# ------------------------------------------------------------
# Key idea:
# This example is intentionally verbose with comments so it can be
# used as GitHub learning material and interview preparation notes.
# ------------------------------------------------------------

from collections import deque
d=deque([10,20,30]); print(d[0], d[-1])
