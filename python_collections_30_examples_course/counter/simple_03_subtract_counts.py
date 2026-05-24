"""
collections.Counter Simple Example 3: Subtract Counts
Difficulty: Simple

Business Question:
Subtract counts.

How to run:
    python simple_03_subtract_counts.py
"""

# ------------------------------------------------------------
# Key idea:
# This example is intentionally verbose with comments so it can be
# used as GitHub learning material and interview preparation notes.
# ------------------------------------------------------------

from collections import Counter
a=Counter({'A':3}); b=Counter({'A':1})
print(a-b)
