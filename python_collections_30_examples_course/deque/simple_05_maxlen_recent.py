"""
collections.deque Simple Example 5: Maxlen Recent
Difficulty: Simple

Business Question:
Keep recent N events.

How to run:
    python simple_05_maxlen_recent.py
"""

# ------------------------------------------------------------
# Key idea:
# This example is intentionally verbose with comments so it can be
# used as GitHub learning material and interview preparation notes.
# ------------------------------------------------------------

from collections import deque
d=deque(maxlen=3)
for x in range(5): d.append(x)
print(d)
