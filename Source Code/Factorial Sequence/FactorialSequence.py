"""
File: FactorialSequence.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    A scholarly implementation of a Factorial sequence generator. This module 
    leverages productive iterative logic to yield a sequence of factorial values 
    for n! within a defined range, optimizing for memory efficiency.

Mathematical Logic:
    The factorial of a non-negative integer n, denoted by n!, is the product 
    of all positive integers less than or equal to n:
    n! = n × (n - 1) × (n - 2) × ... × 1
    0! is defined as 1.
"""

from typing import Generator

def factorial_generator(limit: int) -> Generator[int, None, None]:
    """
    Generates a sequence of factorial values up to the specified limit.

    Args:
        limit (int): The upper bound (inclusive) of integers to calculate factorials for.

    Yields:
        int: The next factorial value in the sequence.

    Raises:
        ValueError: If the limit is negative.
    """
    if limit < 0:
        raise ValueError("Factorial is not defined for negative integers.")

    acc = 1
    yield acc  # 0! = 1
    
    for i in range(1, limit + 1):
        acc *= i
        yield acc

def run_factorial_demo():
    """Execution demo with structured sequence output."""
    print("--- Python Shorts: Combinatorial Sequences (Factorial) ---")
    
    # Boundary and standard cases
    test_limits = [5, 10, 0]
    
    for limit in test_limits:
        print(f"\n[Sequence]: Factorials up to {limit}!")
        try:
            results = list(factorial_generator(limit))
            print(f"[Output]: {results}")
        except ValueError as e:
            print(f"[Error]: {e}")

if __name__ == "__main__":
    run_factorial_demo()
