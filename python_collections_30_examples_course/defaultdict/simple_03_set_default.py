"""
collections.defaultdict Simple Example 3: Set Default
Difficulty: Simple

Business Question:
Group unique values.

How to run:
    python simple_03_set_default.py
"""

# ------------------------------------------------------------
# Key idea:
# This example is intentionally verbose with comments so it can be
# used as GitHub learning material and interview preparation notes.
# ------------------------------------------------------------

from collections import defaultdict
d=defaultdict(set); d['P1'].add('read'); print(dict(d))
