"""
collections.defaultdict Simple Example 2: Count Values
Difficulty: Simple

Business Question:
Count using int default.

How to run:
    python simple_02_count_values.py
"""

# ------------------------------------------------------------
# Key idea:
# This example is intentionally verbose with comments so it can be
# used as GitHub learning material and interview preparation notes.
# ------------------------------------------------------------

from collections import defaultdict
d=defaultdict(int)
for x in ['A','A','B']: d[x]+=1
print(dict(d))
