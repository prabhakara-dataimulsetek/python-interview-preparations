"""
list Simple Example 2: Filter High Values
Difficulty: Simple

Business Question:
Keep values above a threshold.

How to run:
    python simple_02_filter_high_values.py
"""

# ------------------------------------------------------------
# Key idea:
# This example is intentionally verbose with comments so it can be
# used as GitHub learning material and interview preparation notes.
# ------------------------------------------------------------

claims=[100,900,250,1200]
print([c for c in claims if c>=500])


# create filtered_claims list if claim <= 900
filtered_claims = [c for c in claims if c <= 900] 

print(filtered_claims)

# using for loop yield 
filtered_claims = []

for c in claims:
    if c <= 900:
        filtered_claims.append(c)
print(filtered_claims)

# for with yield example
def filtered_claims(claims):
    for c in claims:
        if c <= 900:
            yield c

print(filtered_claims(claims))



