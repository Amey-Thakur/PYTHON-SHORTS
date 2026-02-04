"""
File: FibbonacciSequence.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    A memory-efficient generator for the Fibonacci sequence. This implementation 
    leverages the stateful nature of Python generators to produce sequences of 
    arbitrary length with O(1) space complexity.

Mathematical Logic:
    The Fibonacci sequence F_n is defined by the recurrence relation:
    F_n = F_{n-1} + F_{n-2}
    with seed values F_0 = 0 and F_1 = 1.
"""

from typing import Generator, List

def fibonacci_generator() -> Generator[int, None, None]:
    """
    Stateful generator for the infinite Fibonacci sequence.

    Yields:
        int: The next number in the Fibonacci sequence.
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def generate_fibonacci_sequence(limit: int) -> List[int]:
    """
    Produces a finite slice of the Fibonacci sequence.

    Args:
        limit (int): The number of terms to generate.

    Returns:
        List[int]: A list containing the first 'limit' terms of the sequence.

    Raises:
        ValueError: If the limit is negative.
    """
    if limit < 0:
        raise ValueError("Sequence limit must be non-negative.")
    
    gen = fibonacci_generator()
    return [next(gen) for _ in range(limit)]

def run_fibonacci_demo():
    """Execution demo with standard and boundary test vectors."""
    print("--- Python Shorts: Linear Recurrence Relations (Fibonacci) ---")
    
    test_limits = [0, 1, 5, 10, 15]
    
    for limit in test_limits:
        print(f"\n[Sequence]: First {limit} terms")
        try:
            results = generate_fibonacci_sequence(limit)
            print(f"[Output]: {results}")
        except ValueError as e:
            print(f"[Error]: {e}")

    # Robustness Check
    print("\n[Robustness Check]: Attempting negative limit (-3)")
    try:
        generate_fibonacci_sequence(-3)
    except ValueError as e:
        print(f"[Captured Error]: {e}")

if __name__ == "__main__":
    run_fibonacci_demo()
