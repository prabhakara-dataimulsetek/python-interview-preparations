"""
collections.defaultdict Simple Example 1: Group Names
Difficulty: Simple

Business Question:
Group values by key.

How to run:
    python simple_01_group_names.py
"""

# ------------------------------------------------------------
# Key idea:
# This example is intentionally verbose with comments so it can be
# used as GitHub learning material and interview preparation notes.
# ------------------------------------------------------------

from collections import defaultdict
d=defaultdict(list)
d['cardiology'].append('Dr Rao')
print(dict(d))
