"""
collections.deque Simple Example 6: Extend Values
Difficulty: Simple

Business Question:
Extend deque.

How to run:
    python simple_06_extend_values.py
"""

# ------------------------------------------------------------
# Key idea:
# This example is intentionally verbose with comments so it can be
# used as GitHub learning material and interview preparation notes.
# ------------------------------------------------------------

from collections import deque
d=deque([1]); d.extend([2,3]); print(d)
