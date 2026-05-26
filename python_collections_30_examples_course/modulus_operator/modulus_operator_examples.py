"""
modulus_examples.py

Common Interview Questions Using Modulus Operator (%)

Topics Covered:
1. Even/Odd Check
2. Reverse Integer
3. Palindrome Number
4. Sum of Digits
5. Armstrong Number
6. Circular Array Rotation
7. Cyclic Scheduling
8. Hash Partitioning
9. Leap Year Calculation
10. Clock Angle Problem
"""

# =========================================================
# 1. EVEN / ODD CHECK
# =========================================================

def even_or_odd(num):
    """
    If number divided by 2 leaves remainder 0 -> Even
    Else -> Odd
    """
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


print("\n1. EVEN OR ODD")
print(even_or_odd(10))
print(even_or_odd(7))


# =========================================================
# 2. REVERSE INTEGER
# =========================================================

def reverse_integer(num):
    """
    Reverse digits using modulus operator.
    Example:
    1234 -> 4321
    """
    reversed_num = 0

    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num = num // 10

    return reversed_num


print("\n2. REVERSE INTEGER")
print(reverse_integer(1234))


# =========================================================
# 3. PALINDROME NUMBER
# =========================================================

def is_palindrome(num):
    """
    A palindrome reads same forward and backward.
    Example:
    121 -> palindrome
    123 -> not palindrome
    """
    original = num
    reversed_num = 0

    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num = num // 10

    return original == reversed_num


print("\n3. PALINDROME NUMBER")
print(is_palindrome(121))
print(is_palindrome(123))


# =========================================================
# 4. SUM OF DIGITS
# =========================================================

def sum_of_digits(num):
    """
    Sum all digits in a number.
    Example:
    1234 -> 1+2+3+4 = 10
    """
    total = 0

    while num > 0:
        digit = num % 10
        total += digit
        num = num // 10

    return total


print("\n4. SUM OF DIGITS")
print(sum_of_digits(1234))


# =========================================================
# 5. ARMSTRONG NUMBER
# =========================================================

def is_armstrong(num):
    """
    Armstrong Number:
    Sum of cubes of digits equals original number.

    Example:
    153
    1^3 + 5^3 + 3^3 = 153
    """
    original = num
    total = 0

    while num > 0:
        digit = num % 10
        total += digit ** 3
        num = num // 10

    return original == total


print("\n5. ARMSTRONG NUMBER")
print(is_armstrong(153))
print(is_armstrong(123))


# =========================================================
# 6. CIRCULAR ARRAY ROTATION
# =========================================================

def circular_rotation(arr, k):
    """
    Rotate array using modulus.

    Example:
    [1,2,3,4,5], k=2
    Output:
    [4,5,1,2,3]
    """

    n = len(arr)

    result = [0] * n

    for i in range(n):
        new_index = (i + k) % n
        result[new_index] = arr[i]

    return result


print("\n6. CIRCULAR ARRAY ROTATION")
print(circular_rotation([1, 2, 3, 4, 5], 2))


# =========================================================
# 7. CYCLIC SCHEDULING
# =========================================================

def cyclic_scheduling(tasks, workers):
    """
    Assign tasks to workers in round-robin fashion.

    Uses modulus for cyclic allocation.
    """

    for i in range(tasks):
        worker = workers[i % len(workers)]
        print(f"Task-{i+1} -> {worker}")


print("\n7. CYCLIC SCHEDULING")
workers_list = ["Worker-A", "Worker-B", "Worker-C"]
cyclic_scheduling(10, workers_list)


# =========================================================
# 8. HASH PARTITIONING
# =========================================================

def hash_partitioning(record_id, total_partitions):
    """
    Common in Spark/Kafka/Databases.

    Distribute records evenly.
    """
    return record_id % total_partitions


print("\n8. HASH PARTITIONING")
print("Record 105 goes to partition:",
      hash_partitioning(105, 5))


# =========================================================
# 9. LEAP YEAR CALCULATION
# =========================================================

def is_leap_year(year):
    """
    Leap year rules:
    1. Divisible by 400 -> leap
    2. Divisible by 4 and not by 100 -> leap
    """

    if year % 400 == 0:
        return True

    if year % 4 == 0 and year % 100 != 0:
        return True

    return False


print("\n9. LEAP YEAR")
print(is_leap_year(2024))
print(is_leap_year(2025))


# =========================================================
# 10. CLOCK ANGLE PROBLEM
# =========================================================

def clock_angle(hour, minute):
    """
    Find angle between hour and minute hands.

    Formula:
    Hour hand moves:
        0.5 degree per minute

    Minute hand moves:
        6 degrees per minute
    """

    hour_angle = (hour % 12) * 30 + minute * 0.5
    minute_angle = minute * 6

    angle = abs(hour_angle - minute_angle)

    return min(angle, 360 - angle)


print("\n10. CLOCK ANGLE")
print(clock_angle(3, 30))
print(clock_angle(9, 45))


# =========================================================
# END
# =========================================================

print("\nAll modulus examples completed successfully.")