"""
dict Simple Example 5: Invert Dict
Difficulty: Simple

Business Question:
Invert keys and values.

How to run:
    python simple_05_invert_dict.py
"""

# ------------------------------------------------------------
# Key idea:
# This example is intentionally verbose with comments so it can be
# used as GitHub learning material and interview preparation notes.
# ------------------------------------------------------------

d={'P1':'Anita','P2':'Ravi'}
print({v:k for k,v in d.items()})
