"""
File: EvenNumberGenerator.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    A memory-efficient sequence generator for arithmetic progressions of even 
    integers. This implementation leverages Python's generator protocol for 
    lazy evaluation, enabling the production of potentially infinite 
    sequences with O(1) space complexity.

Mathematical Logic:
    An integer n is even if n ≡ 0 (mod 2). This generator produces the sequence 
    S = {s_i | s_i = 2k_i, k_i ∈ ℤ} for a defined range or infinite progression.
"""

from typing import Generator, Optional

class GeneratorError(Exception):
    """Exception raised for invalid generator parameters."""
    pass

def generate_even_numbers(limit: Optional[int] = None, start: int = 0) -> Generator[int, None, None]:
    """
    Generates a sequence of even integers using lazy evaluation.

    Args:
        limit (Optional[int]): The exclusive upper bound for the sequence. 
                               If None, the generator is infinite.
        start (int): The starting integer value. If odd, the sequence 
                     shifts to the next even integer.

    Yields:
        int: The next even integer in the sequence.

    Raises:
        GeneratorError: If the input parameters are not of type 'int'.
    """
    if not isinstance(start, int):
        raise GeneratorError("Initial sequence value must be an integer.")
    
    if limit is not None and not isinstance(limit, int):
        raise GeneratorError("Sequence limit must be an integer or None.")

    # Align starting value to the next even integer if necessary
    current = start if start % 2 == 0 else start + 1
    
    while limit is None or current < limit:
        yield current
        current += 2

def run_generator_demo():
    """Execution demo with finite and boundary test vectors."""
    print("--- Python Shorts: Arithmetic Progression (Even Number Generator) ---")
    
    print("\n[Sequence]: Even integers in range [0, 20):")
    for num in generate_even_numbers(limit=20):
        print(num, end=" ")
    
    print("\n\n[Sequence]: Transition from odd starting point (start=5, limit=15):")
    for num in generate_even_numbers(limit=15, start=5):
        print(num, end=" ")
    
    print("\n\n[Sequence]: Boundary Case (limit=0):")
    for num in generate_even_numbers(limit=0):
        print(num, end=" ")
    print("(Empty)")

    print("\n[Sequence]: Robustness Check (start='A'):")
    try:
        next(generate_even_numbers(start="A")) # type: ignore
    except GeneratorError as e:
        print(f"Error captured: {e}")

if __name__ == "__main__":
    run_generator_demo()
