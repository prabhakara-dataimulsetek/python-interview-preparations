"""
collections.defaultdict Simple Example 9: Convert To Dict
Difficulty: Simple

Business Question:
Convert defaultdict to normal dict.

How to run:
    python simple_09_convert_to_dict.py
"""

# ------------------------------------------------------------
# Key idea:
# This example is intentionally verbose with comments so it can be
# used as GitHub learning material and interview preparation notes.
# ------------------------------------------------------------

from collections import defaultdict
d=defaultdict(list); d['x'].append(1)
print(dict(d))
