"""
list Simple Example 2: Filter High Values
Difficulty: Simple

Business Question:
Keep values above a threshold.

How to run:
    python simple_02_filter_high_values.py
"""

# ------------------------------------------------------------
# Key idea:
# This example is intentionally verbose with comments so it can be
# used as GitHub learning material and interview preparation notes.
# ------------------------------------------------------------

claims=[100,900,250,1200]
print([c for c in claims if c>=500])
