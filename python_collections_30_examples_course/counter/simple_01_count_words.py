"""
collections.Counter Simple Example 1: Count Words
Difficulty: Simple

Business Question:
Count word frequency.

How to run:
    python simple_01_count_words.py
"""

# ------------------------------------------------------------
# Key idea:
# This example is intentionally verbose with comments so it can be
# used as GitHub learning material and interview preparation notes.
# ------------------------------------------------------------

from collections import Counter
text='claim claim benefit'
print(Counter(text.split()))
