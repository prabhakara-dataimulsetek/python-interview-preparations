"""
dict Simple Example 9: Dict Comprehension
Difficulty: Simple

Business Question:
Build dict using comprehension.

How to run:
    python simple_09_dict_comprehension.py
"""

# ------------------------------------------------------------
# Key idea:
# This example is intentionally verbose with comments so it can be
# used as GitHub learning material and interview preparation notes.
# ------------------------------------------------------------

nums=[1,2,3]
print({n:n*n for n in nums})

"""
dict Simple Example 9: Dict Comprehension
Difficulty: Simple

Business Question:
A data engineering team wants to quickly generate lookup mappings
for IDs and their calculated metrics. Build a dictionary using
dictionary comprehension.

Real-world use cases:
- Employee ID -> Salary
- Product ID -> Price
- Customer ID -> Score
- Number -> Square value

How to run:
    python simple_09_dict_comprehension.py
"""

# ------------------------------------------------------------
# WHAT IS DICTIONARY COMPREHENSION?
# ------------------------------------------------------------
#
# Dictionary comprehension is a concise way to create dictionaries.
#
# Syntax:
#
# {
#     key_expression : value_expression
#     for item in iterable
# }
#
# ------------------------------------------------------------
# NORMAL LOOP VERSION
# ------------------------------------------------------------

nums = [1, 2, 3]

square_dict = {}

for n in nums:
    square_dict[n] = n * n

print("Using normal loop:")
print(square_dict)

# Output:
# {1: 1, 2: 4, 3: 9}

# ------------------------------------------------------------
# DICTIONARY COMPREHENSION VERSION
# ------------------------------------------------------------

nums = [1, 2, 3]

square_dict = {n: n * n for n in nums}

print("\nUsing dictionary comprehension:")
print(square_dict)

# Output:
# {1: 1, 2: 4, 3: 9}

# ------------------------------------------------------------
# STEP-BY-STEP BREAKDOWN
# ------------------------------------------------------------
#
# {n: n*n for n in nums}
#
# n           -> key
# n*n         -> value
# for n in nums -> loop through list
#
# Iteration Flow:
#
# n = 1 -> 1:1
# n = 2 -> 2:4
# n = 3 -> 3:9
#
# Final dictionary:
# {
#   1: 1,
#   2: 4,
#   3: 9
# }
#
# ------------------------------------------------------------
# EXAMPLE 2: EVEN NUMBERS ONLY
# ------------------------------------------------------------

even_squares = {
    n: n * n
    for n in range(10)
    if n % 2 == 0
}

print("\nEven squares:")
print(even_squares)

# Output:
# {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# ------------------------------------------------------------
# EXAMPLE 3: STRING LENGTH MAPPING
# ------------------------------------------------------------

names = ["John", "Mary", "David"]

name_lengths = {
    name: len(name)
    for name in names
}

print("\nName lengths:")
print(name_lengths)

# Output:
# {
#   'John': 4,
#   'Mary': 4,
#   'David': 5
# }

# ------------------------------------------------------------
# EXAMPLE 4: LOWERCASE TO UPPERCASE
# ------------------------------------------------------------

fruits = {
    "a": "apple",
    "b": "banana"
}

upper_fruits = {
    k: v.upper()
    for k, v in fruits.items()
}

print("\nUppercase values:")
print(upper_fruits)

# Output:
# {
#   'a': 'APPLE',
#   'b': 'BANANA'
# }

# ------------------------------------------------------------
# EXAMPLE 5: SWAP KEYS AND VALUES
# ------------------------------------------------------------

student = {
    "id": 101,
    "name": "Prabha"
}

reversed_dict = {
    v: k
    for k, v in student.items()
}

print("\nReversed dictionary:")
print(reversed_dict)

# Output:
# {
#   101: 'id',
#   'Prabha': 'name'
# }

# ------------------------------------------------------------
# INTERVIEW QUESTIONS
# ------------------------------------------------------------

# Q1: Why use dictionary comprehension?
#
# Answer:
# - Cleaner code
# - Shorter syntax
# - Faster execution
# - Easier transformations

# Q2: Can we use conditions?
#
# Yes:
#
# {x: x*x for x in range(10) if x > 5}

# Q3: Difference between list comprehension and dict comprehension?
#
# List comprehension:
# [x*x for x in nums]
#
# Dict comprehension:
# {x: x*x for x in nums}

# ------------------------------------------------------------
# COMMON MISTAKE
# ------------------------------------------------------------

# WRONG:
#
# {n*n for n in nums}
#
# This creates a SET, not a dictionary.

# CORRECT:
#
# {n: n*n for n in nums}

# ------------------------------------------------------------
# FINAL TAKEAWAY
# ------------------------------------------------------------
#
# Dictionary comprehension is heavily used in:
#
# - PySpark transformations
# - JSON processing
# - API response normalization
# - Data engineering pipelines
# - ETL mapping logic
# - Feature engineering
#
# It is a very common Python interview topic.
#
# ------------------------------------------------------------
