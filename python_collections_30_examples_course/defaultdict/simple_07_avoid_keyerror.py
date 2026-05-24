"""
collections.defaultdict Simple Example 7: Avoid Keyerror
Difficulty: Simple

Business Question:
No KeyError for missing key.

How to run:
    python simple_07_avoid_keyerror.py
"""

# ------------------------------------------------------------
# Key idea:
# This example is intentionally verbose with comments so it can be
# used as GitHub learning material and interview preparation notes.
# ------------------------------------------------------------

from collections import defaultdict
d=defaultdict(list)
print(d['missing'])
