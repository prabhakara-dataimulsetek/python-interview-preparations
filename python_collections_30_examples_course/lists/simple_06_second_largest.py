"""
list Simple Example 6: Second Largest
Difficulty: Simple

Business Question:
Find the second largest distinct value.

How to run:
    python simple_06_second_largest.py
"""

# ------------------------------------------------------------
# Key idea:
# This example is intentionally verbose with comments so it can be
# used as GitHub learning material and interview preparation notes.
# ------------------------------------------------------------

nums=[10,4,10,8,2]
print(sorted(set(nums))[-2])
