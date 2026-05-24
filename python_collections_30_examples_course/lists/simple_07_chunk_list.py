"""
list Simple Example 7: Chunk List
Difficulty: Simple

Business Question:
Split list into chunks of size 3.

How to run:
    python simple_07_chunk_list.py
"""

# ------------------------------------------------------------
# Key idea:
# This example is intentionally verbose with comments so it can be
# used as GitHub learning material and interview preparation notes.
# ------------------------------------------------------------

items=list(range(1,10))
print([items[i:i+3] for i in range(0,len(items),3)])
