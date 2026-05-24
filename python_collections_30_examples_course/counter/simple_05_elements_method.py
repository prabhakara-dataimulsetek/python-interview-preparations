"""
collections.Counter Simple Example 5: Elements Method
Difficulty: Simple

Business Question:
Expand counts to elements.

How to run:
    python simple_05_elements_method.py
"""

# ------------------------------------------------------------
# Key idea:
# This example is intentionally verbose with comments so it can be
# used as GitHub learning material and interview preparation notes.
# ------------------------------------------------------------

from collections import Counter
print(list(Counter({'A':2,'B':1}).elements()))
