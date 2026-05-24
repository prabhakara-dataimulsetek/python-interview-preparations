"""
collections.Counter Simple Example 10: Total Count
Difficulty: Simple

Business Question:
Sum all counts.

How to run:
    python simple_10_total_count.py
"""

# ------------------------------------------------------------
# Key idea:
# This example is intentionally verbose with comments so it can be
# used as GitHub learning material and interview preparation notes.
# ------------------------------------------------------------

from collections import Counter
c=Counter(['a','b','a'])
print(sum(c.values()))
