"""
tuple Simple Example 9: Named Tuple Basic
Difficulty: Simple

Business Question:
Use namedtuple for readable records.

How to run:
    python simple_09_named_tuple_basic.py
"""

# ------------------------------------------------------------
# Key idea:
# This example is intentionally verbose with comments so it can be
# used as GitHub learning material and interview preparation notes.
# ------------------------------------------------------------

from collections import namedtuple
Patient=namedtuple('Patient','id name')
p=Patient('P1','Ravi')
print(p.name)
