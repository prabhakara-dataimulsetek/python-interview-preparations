"""
list Simple Example 1: Sum Daily Calls
Difficulty: Simple

Business Question:
Calculate total calls from a list.

How to run:
    python simple_01_sum_daily_calls.py
"""

# ------------------------------------------------------------
# Key idea:
# This example is intentionally verbose with comments so it can be
# used as GitHub learning material and interview preparation notes.
# ------------------------------------------------------------

calls=[12,18,7,25]
print(sum(calls))

sum = 0
for call in calls:
    sum += call
print(sum)