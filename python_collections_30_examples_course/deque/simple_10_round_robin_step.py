"""
collections.deque Simple Example 10: Round Robin Step
Difficulty: Simple

Business Question:
Simple round-robin rotation.

How to run:
    python simple_10_round_robin_step.py
"""

# ------------------------------------------------------------
# Key idea:
# This example is intentionally verbose with comments so it can be
# used as GitHub learning material and interview preparation notes.
# ------------------------------------------------------------

from collections import deque
agents=deque(['A','B','C']); agents.rotate(-1); print(agents[0])
