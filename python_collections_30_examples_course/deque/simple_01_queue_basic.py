"""
collections.deque Simple Example 1: Queue Basic
Difficulty: Simple

Business Question:
Use deque as queue.

How to run:
    python simple_01_queue_basic.py
"""

# ------------------------------------------------------------
# Key idea:
# This example is intentionally verbose with comments so it can be
# used as GitHub learning material and interview preparation notes.
# ------------------------------------------------------------

from collections import deque
q=deque(['call1']); q.append('call2'); print(q.popleft())
