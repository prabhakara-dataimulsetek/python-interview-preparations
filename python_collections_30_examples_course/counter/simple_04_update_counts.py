"""
collections.Counter Simple Example 4: Update Counts
Difficulty: Simple

Business Question:
Update counts incrementally.

How to run:
    python simple_04_update_counts.py
"""

# ------------------------------------------------------------
# Key idea:
# This example is intentionally verbose with comments so it can be
# used as GitHub learning material and interview preparation notes.
# ------------------------------------------------------------

from collections import Counter
c=Counter(); c.update(['x','x','y']); print(c)
