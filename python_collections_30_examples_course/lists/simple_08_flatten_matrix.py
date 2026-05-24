"""
list Simple Example 8: Flatten Matrix
Difficulty: Simple

Business Question:
Flatten a 2D list.

How to run:
    python simple_08_flatten_matrix.py
"""

# ------------------------------------------------------------
# Key idea:
# This example is intentionally verbose with comments so it can be
# used as GitHub learning material and interview preparation notes.
# ------------------------------------------------------------

matrix=[[1,2],[3,4],[5]]
print([x for row in matrix for x in row])
