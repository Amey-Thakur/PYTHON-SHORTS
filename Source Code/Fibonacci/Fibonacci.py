"""
File: Fibonacci.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    A high-fidelity implementation for calculating the n-th Fibonacci number. 
    This module provides optimized iterative logic and a memoized recursive 
    alternative, demonstrating algorithmic efficiency and state management.

Mathematical Logic:
    The Fibonacci sequence satisfies the recurrence: F_n = F_{n-1} + F_{n-2}.
    This module computes the n-th term with O(n) time and O(1) space 
    complexities using iterative state updates.
"""

from typing import Dict, Optional

def fibonacci_iterative(n: int) -> int:
    """
    Computes the n-th Fibonacci number using an optimized iterative approach.

    Args:
        n (int): The position in the sequence (0-indexed).

    Returns:
        int: The n-th Fibonacci number.

    Raises:
        ValueError: If n is negative.
        TypeError: If n is not an integer.
    """
    if not isinstance(n, int):
        raise TypeError(f"Input must be an integer, received {type(n).__name__}.")
    if n < 0:
        raise ValueError("Fibonacci is undefined for negative indices.")
    
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def fibonacci_memoized(n: int, memo: Optional[Dict[int, int]] = None) -> int:
    """
    Computes the n-th Fibonacci number using recursion with memoization.

    Args:
        n (int): The position in the sequence.
        memo (Optional[Dict[int, int]]): Dictionary for result caching.

    Returns:
        int: The n-th Fibonacci number.
    """
    if memo is None:
        memo = {0: 0, 1: 1}
    
    if n in memo:
        return memo[n]
    
    memo[n] = fibonacci_memoized(n - 1, memo) + fibonacci_memoized(n - 2, memo)
    return memo[n]

def run_fibonacci_demo():
    """Execution demo showcasing computational methods and boundary states."""
    print("--- Python Shorts: Recurrence Relations (Fibonacci) ---")
    
    test_values = [0, 1, 5, 10, 20]
    
    print("\n[Method]: Iterative Computation (O(n) Time, O(1) Space)")
    for val in test_values:
        print(f"F({val}) = {fibonacci_iterative(val)}")
        
    print("\n[Method]: Memoized Recursion (O(n) Time, O(n) Space)")
    for val in test_values:
        print(f"F({val}) = {fibonacci_memoized(val)}")

    # Robustness Check
    print("\n[Robustness Check]: Attempting negative index (-5)")
    try:
        fibonacci_iterative(-5)
    except ValueError as e:
        print(f"[Captured Error]: {e}")

if __name__ == "__main__":
    run_fibonacci_demo()
