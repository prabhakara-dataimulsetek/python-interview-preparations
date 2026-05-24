"""
collections.defaultdict Simple Example 8: Default Factory Demo
Difficulty: Simple

Business Question:
Show default factory.

How to run:
    python simple_08_default_factory_demo.py
"""

# ------------------------------------------------------------
# Key idea:
# This example is intentionally verbose with comments so it can be
# used as GitHub learning material and interview preparation notes.
# ------------------------------------------------------------

from collections import defaultdict
d=defaultdict(int)
print(d.default_factory)
