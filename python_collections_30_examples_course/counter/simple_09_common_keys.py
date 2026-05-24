"""
collections.Counter Simple Example 9: Common Keys
Difficulty: Simple

Business Question:
Counter intersection.

How to run:
    python simple_09_common_keys.py
"""

# ------------------------------------------------------------
# Key idea:
# This example is intentionally verbose with comments so it can be
# used as GitHub learning material and interview preparation notes.
# ------------------------------------------------------------

from collections import Counter
print(Counter({'A':3,'B':1}) & Counter({'A':1,'C':2}))
