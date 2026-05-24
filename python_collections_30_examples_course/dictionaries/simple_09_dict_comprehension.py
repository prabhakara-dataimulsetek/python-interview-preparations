"""
dict Simple Example 9: Dict Comprehension
Difficulty: Simple

Business Question:
Build dict using comprehension.

How to run:
    python simple_09_dict_comprehension.py
"""

# ------------------------------------------------------------
# Key idea:
# This example is intentionally verbose with comments so it can be
# used as GitHub learning material and interview preparation notes.
# ------------------------------------------------------------

nums=[1,2,3]
print({n:n*n for n in nums})
