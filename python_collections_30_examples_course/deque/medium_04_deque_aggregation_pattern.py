"""
collections.deque Medium Example 4: Aggregation Pattern
Difficulty: Medium

Business Question:
Use collections.deque to solve an aggregation/ranking business problem.

How to run:
    python medium_04_deque_aggregation_pattern.py
"""

# ------------------------------------------------------------
# Key idea:
# This example is intentionally verbose with comments so it can be
# used as GitHub learning material and interview preparation notes.
# ------------------------------------------------------------

def solve(records):
    # Medium pattern: aggregate records, then sort by business rule.
    # Input records are tuples: (key, value).
    totals = {}
    for key, value in records:
        totals[key] = totals.get(key, 0) + value
    # Sort by total descending, then key ascending for deterministic output.
    return sorted(totals.items(), key=lambda item: (-item[1], item[0]))

if __name__ == '__main__':
    sample = [('A', 10), ('B', 5), ('A', 7), ('C', 20)]
    print(solve(sample))

# deque note: use deque when input arrives as a stream or queue.

