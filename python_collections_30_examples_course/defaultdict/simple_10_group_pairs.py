"""
collections.defaultdict Simple Example 10: Group Pairs
Difficulty: Simple

Business Question:
Group tuple pairs.

How to run:
    python simple_10_group_pairs.py
"""

# ------------------------------------------------------------
# Key idea:
# This example is intentionally verbose with comments so it can be
# used as GitHub learning material and interview preparation notes.
# ------------------------------------------------------------

from collections import defaultdict
d=defaultdict(list)
for k,v in [('a',1),('a',2)]: d[k].append(v)
print(dict(d))
