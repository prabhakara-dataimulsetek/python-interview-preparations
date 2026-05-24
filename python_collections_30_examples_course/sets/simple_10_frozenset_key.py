"""
set Simple Example 10: Frozenset Key
Difficulty: Simple

Business Question:
Use frozenset as dictionary key.

How to run:
    python simple_10_frozenset_key.py
"""

# ------------------------------------------------------------
# Key idea:
# This example is intentionally verbose with comments so it can be
# used as GitHub learning material and interview preparation notes.
# ------------------------------------------------------------

d={frozenset({'A','B'}): 'group1'}
print(d)
