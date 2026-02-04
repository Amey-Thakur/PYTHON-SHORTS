"""
File: Factorial.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    A high-fidelity implementation for calculating the factorial of a 
    non-negative integer. This module provides both recursive and iterative 
    methodologies, optimized for mathematical precision and algorithmic 
    robustness.

Mathematical Logic:
    n! = n × (n - 1) × (n - 2) × ... × 1
    0! = 1 (defined by convention for combinatorial consistency).
"""

import sys

def factorial(n: int) -> int:
    """
    Computes the factorial of a non-negative integer using iterative logic.
    
    Iteration is preferred over recursion in standard Python for large n 
    to avoid exceeding the recursion depth limit.

    Args:
        n (int): The integer value to compute.

    Returns:
        int: The factorial value (n!).

    Raises:
        ValueError: If the input integer is negative.
        TypeError: If the input is not an integer.
    """
    if not isinstance(n, int):
        raise TypeError(f"Factorial input must be an integer, received {type(n).__name__}.")
    
    if n < 0:
        raise ValueError("Factorial is undefined for negative integers.")

    if n == 0 or n == 1:
        return 1

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def run_factorial_demo():
    """Execution demo with standard and boundary mathematical test vectors."""
    print("--- Python Shorts: Recursive Function Theory (Factorial) ---")
    
    test_cases = [0, 1, 5, 10, 15]
    
    for val in test_cases:
        print(f"[Input]: {val}! | [Result]: {factorial(val)}")

    # Robustness Check
    print("\n[Robustness Check]: Attempting negative input (-5)")
    try:
        factorial(-5)
    except ValueError as e:
        print(f"[Captured Error]: {e}")

if __name__ == "__main__":
    run_factorial_demo()
