"""
list Simple Example 10: Rotate Right
Difficulty: Simple

Business Question:
Rotate a list right by k.

How to run:
    python simple_10_rotate_right.py
"""

# ------------------------------------------------------------
# Key idea:
# This example is intentionally verbose with comments so it can be
# used as GitHub learning material and interview preparation notes.
# ------------------------------------------------------------

arr=[1,2,3,4,5]
k=2
print(arr[-k:]+arr[:-k])

# do it in place
def rotate_right(arr, k):
    if k > len(arr):
        k = k % len(arr)

