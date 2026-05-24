# Problem 1: Array Window Stabilizer

**Topic:** Python `lists` collections  
**Difficulty:** Medium to Complex

## Real Business Question
Given daily risk scores, find the longest contiguous segment where max-min <= K.

## Input Style
Design the input similar to HackerRank: first line contains counts/limits, followed by records. Use clear whitespace-separated or JSON-like rows.

## Output Style
Return the requested records or metric in deterministic sorted order.

## Constraints
- Up to 100,000 records unless otherwise stated
- Optimize for O(n), O(n log n), or sliding-window complexity
- Avoid nested O(n²) loops unless input size is small

## Example
```text
Sample input:
5
...

Sample output:
...
```

## Expected Collection Pattern
Use two monotonic deques or sorted window logic; demonstrates list/window reasoning.

## Interview Explanation
Explain why this collection is appropriate, how duplicates/ties are handled, and what the time/space complexity is.

## Edge Cases
- Empty input
- Duplicate records
- Tie-breaking
- Missing keys/null values
- Very large input
