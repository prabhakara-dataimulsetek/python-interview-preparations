"""
dict Simple Example 7: Sort By Value
Difficulty: Simple

Business Question:
Sort dictionary by value.

How to run:
    python simple_07_sort_by_value.py
"""

# ------------------------------------------------------------
# Key idea:
# This example is intentionally verbose with comments so it can be
# used as GitHub learning material and interview preparation notes.
# ------------------------------------------------------------

d={'A':3,'B':1}
print(sorted(d.items(), key=lambda x:x[1]))
