"""
collections.defaultdict Simple Example 6: Sum By Key
Difficulty: Simple

Business Question:
Sum amount by department.

How to run:
    python simple_06_sum_by_key.py
"""

# ------------------------------------------------------------
# Key idea:
# This example is intentionally verbose with comments so it can be
# used as GitHub learning material and interview preparation notes.
# ------------------------------------------------------------

from collections import defaultdict
d=defaultdict(float)
for k,a in [('ER',10.5),('ER',2)]: d[k]+=a
print(dict(d))
