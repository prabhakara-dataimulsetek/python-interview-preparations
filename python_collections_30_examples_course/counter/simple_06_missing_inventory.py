"""
collections.Counter Simple Example 6: Missing Inventory
Difficulty: Simple

Business Question:
Find shortages with Counter.

How to run:
    python simple_06_missing_inventory.py
"""

# ------------------------------------------------------------
# Key idea:
# This example is intentionally verbose with comments so it can be
# used as GitHub learning material and interview preparation notes.
# ------------------------------------------------------------

from collections import Counter
need=Counter({'mask':5}); stock=Counter({'mask':2})
print(need-stock)
