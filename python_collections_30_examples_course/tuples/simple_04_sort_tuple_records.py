"""
tuple Simple Example 4: Sort Tuple Records
Difficulty: Simple

Business Question:
Sort records by score.

How to run:
    python simple_04_sort_tuple_records.py
"""

# ------------------------------------------------------------
# Key idea:
# This example is intentionally verbose with comments so it can be
# used as GitHub learning material and interview preparation notes.
# ------------------------------------------------------------

rows=[('A',90),('B',75),('C',90)]
print(sorted(rows,key=lambda x:x[1], reverse=True))
