"""
list Simple Example 9: Index Lookup
Difficulty: Simple

Business Question:
Find index of an item safely.

How to run:
    python simple_09_index_lookup.py
"""

# ------------------------------------------------------------
# Key idea:
# This example is intentionally verbose with comments so it can be
# used as GitHub learning material and interview preparation notes.
# ------------------------------------------------------------

codes=['A10','B20','C30']
target='B20'
print(codes.index(target) if target in codes else -1)
