# Problem 21: Claim Frequency Analyzer

**Topic:** Python `collections` collections  
**Difficulty:** Medium to Complex

## Real Business Question
Find top N claim codes by frequency, tie by code asc.

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
Use collections.Counter.

## Interview Explanation
Explain why this collection is appropriate, how duplicates/ties are handled, and what the time/space complexity is.

## Edge Cases
- Empty input
- Duplicate records
- Tie-breaking
- Missing keys/null values
- Very large input
