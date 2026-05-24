"""
collections.deque Simple Example 2: Stack Basic
Difficulty: Simple

Business Question:
Use deque as stack.

How to run:
    python simple_02_stack_basic.py
"""

# ------------------------------------------------------------
# Key idea:
# This example is intentionally verbose with comments so it can be
# used as GitHub learning material and interview preparation notes.
# ------------------------------------------------------------

from collections import deque
s=deque(); s.append('A'); s.append('B'); print(s.pop())
