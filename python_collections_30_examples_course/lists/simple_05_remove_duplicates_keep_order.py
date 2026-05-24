"""
list Simple Example 5: Remove Duplicates Keep Order
Difficulty: Simple

Business Question:
Remove duplicates while keeping first occurrence.

How to run:
    python simple_05_remove_duplicates_keep_order.py
"""

# ------------------------------------------------------------
# Key idea:
# This example is intentionally verbose with comments so it can be
# used as GitHub learning material and interview preparation notes.
# ------------------------------------------------------------

ids=['A','B','A','C','B']
seen=[]
for x in ids:
    if x not in seen:
        seen.append(x)
print(seen)
