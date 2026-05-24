"""
collections.Counter Simple Example 8: Combine Counters
Difficulty: Simple

Business Question:
Add counters.

How to run:
    python simple_08_combine_counters.py
"""

# ------------------------------------------------------------
# Key idea:
# This example is intentionally verbose with comments so it can be
# used as GitHub learning material and interview preparation notes.
# ------------------------------------------------------------

from collections import Counter
print(Counter({'A':1})+Counter({'A':2,'B':1}))
