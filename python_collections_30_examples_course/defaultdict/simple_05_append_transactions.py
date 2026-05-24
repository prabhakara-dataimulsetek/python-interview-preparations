"""
collections.defaultdict Simple Example 5: Append Transactions
Difficulty: Simple

Business Question:
Collect transactions per user.

How to run:
    python simple_05_append_transactions.py
"""

# ------------------------------------------------------------
# Key idea:
# This example is intentionally verbose with comments so it can be
# used as GitHub learning material and interview preparation notes.
# ------------------------------------------------------------

from collections import defaultdict
d=defaultdict(list); d['U1'] += [100,200]; print(dict(d))
