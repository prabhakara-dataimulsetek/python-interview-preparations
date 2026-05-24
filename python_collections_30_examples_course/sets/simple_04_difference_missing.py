"""
set Simple Example 4: Difference Missing
Difficulty: Simple

Business Question:
Find missing documents.

How to run:
    python simple_04_difference_missing.py
"""

# ------------------------------------------------------------
# Key idea:
# This example is intentionally verbose with comments so it can be
# used as GitHub learning material and interview preparation notes.
# ------------------------------------------------------------

required={'id','insurance','consent'}
submitted={'id'}
print(required-submitted)
