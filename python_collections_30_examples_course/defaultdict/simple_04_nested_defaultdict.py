"""
collections.defaultdict Simple Example 4: Nested Defaultdict
Difficulty: Simple

Business Question:
Nested grouping.

How to run:
    python simple_04_nested_defaultdict.py
"""

# ------------------------------------------------------------
# Key idea:
# This example is intentionally verbose with comments so it can be
# used as GitHub learning material and interview preparation notes.
# ------------------------------------------------------------

from collections import defaultdict
d=defaultdict(lambda: defaultdict(int)); d['A']['x']+=1; print(d['A']['x'])
