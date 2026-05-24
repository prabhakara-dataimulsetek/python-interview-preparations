"""
collections.defaultdict Medium Example 7: Aggregation Pattern
Difficulty: Medium

Business Question:
Use collections.defaultdict to solve an aggregation/ranking business problem.

How to run:
    python medium_07_defaultdict_aggregation_pattern.py
"""

# ------------------------------------------------------------
# Key idea:
# This example is intentionally verbose with comments so it can be
# used as GitHub learning material and interview preparation notes.
# ------------------------------------------------------------

from collections import defaultdict

def solve(records):
    # Medium pattern: aggregate records, then sort by business rule.
    # Input records are tuples: (key, value).
    totals = defaultdict(int)
    for key, value in records:
        totals[key] += value
    # Sort by total descending, then key ascending for deterministic output.
    return sorted(totals.items(), key=lambda item: (-item[1], item[0]))

if __name__ == '__main__':
    sample = [('A', 10), ('B', 5), ('A', 7), ('C', 20)]
    print(solve(sample))

