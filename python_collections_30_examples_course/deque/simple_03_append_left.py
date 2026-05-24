"""
collections.deque Simple Example 3: Append Left
Difficulty: Simple

Business Question:
Add to front.

How to run:
    python simple_03_append_left.py
"""

# ------------------------------------------------------------
# Key idea:
# This example is intentionally verbose with comments so it can be
# used as GitHub learning material and interview preparation notes.
# ------------------------------------------------------------

from collections import deque
d=deque([2,3]); d.appendleft(1); print(d)
