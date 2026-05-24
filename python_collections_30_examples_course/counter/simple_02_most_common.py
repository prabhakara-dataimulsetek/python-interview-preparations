"""
collections.Counter Simple Example 2: Most Common
Difficulty: Simple

Business Question:
Find most common items.

How to run:
    python simple_02_most_common.py
"""

# ------------------------------------------------------------
# Key idea:
# This example is intentionally verbose with comments so it can be
# used as GitHub learning material and interview preparation notes.
# ------------------------------------------------------------

from collections import Counter
print(Counter(['A','B','A']).most_common(1))
