"""
File: ArmstrongNumber.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    An Armstrong number (or Narcissistic number) is a number that is the 
    sum of its own digits each raised to the power of the number of digits.
    Example: 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153.

Complexity Analysis:
    - Time Complexity: O(log10(N)) for checking a single number (where N is the value).
    - Space Complexity: O(log10(N)) to store string representation of digits.

Logic:
    1. Validate that the input is a non-negative integer.
    2. Convert the number to a string to isolate digits and determine the count (k).
    3. Calculate the sum of each digit raised to the k-th power.
    4. Compare the sum with the original number.
"""

import math
from typing import List

class ArmstrongError(Exception):
    """Custom exception for Armstrong Number utility errors."""
    pass

def is_armstrong(number: int) -> bool:
    """
    Checks if a given non-negative integer is an Armstrong number.

    Args:
        number (int): The integer to verify.

    Returns:
        bool: True if it is an Armstrong number, False otherwise.

    Raises:
        ArmstrongError: If input is negative or not an integer.
    """
    if not isinstance(number, int) or number < 0:
        raise ArmstrongError("Input must be a non-negative integer.")

    num_str = str(number)
    num_digits = len(num_str)
    
    # Calculate sum of digits raised to the power of total digits
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    
    return armstrong_sum == number

def find_armstrong_in_range(start: int, end: int) -> List[int]:
    """
    Finds all Armstrong numbers within a specified range [start, end].

    Args:
        start (int): Start of range (inclusive).
        end (int): End of range (inclusive).

    Returns:
        List[int]: List of discovered Armstrong numbers.
    """
    results = []
    for num in range(start, end + 1):
        if is_armstrong(num):
            results.append(num)
    return results

def run_armstrong_demo() -> None:
    """Demonstrates Armstrong number verification and range search."""
    print("--- Python Shorts: Armstrong Number Demo ---")
    test_val = 153
    print(f"Is {test_val} an Armstrong number? {is_armstrong(test_val)}")
    
    search_range = (100, 1000)
    print(f"Armstrong numbers in range {search_range}: {find_armstrong_in_range(*search_range)}")

if __name__ == '__main__':
    run_armstrong_demo()