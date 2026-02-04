"""
File: Power2Sequence.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    A high-fidelity computational utility for generating a sequence of powers 
    of two. This module utilizes bitwise left-shift operations to achieve 
    maximum efficiency in base-2 calculations.

Mathematical Logic:
    A power of two is any number of the form 2^n, where n is an integer. 
    In binary representation, 2^n is represented as a '1' followed by n '0's. 
    This can be calculated using the bitwise left-shift operator: 
    1 << n = 2^n.
"""

from typing import List

class PowerSequenceGenerator:
    """Scholarly implementation of binary power sequence generation."""

    @staticmethod
    def generate_sequence(limit: int) -> List[int]:
        """
        Generates a sequence of powers of two from 2^0 up to 2^(limit-1).

        Args:
            limit (int): The number of terms to generate.

        Returns:
            List[int]: The generated sequence.
        """
        if limit < 0:
            return []

        # Bitwise shift (1 << i) is O(1) and more efficient than 2 ** i
        sequence = [1 << i for i in range(limit)]
        return sequence

def run_power_demo():
    """Execution demo showcasing bitwise sequence generation."""
    print("--- Python Shorts: Power of Two Sequence Generator ---")
    
    # Generate sequence for 2^0 through 2^15
    term_count = 16
    print(f"[Input]: Requesting {term_count} terms (2^0 to 2^{term_count-1})")
    
    sequence = PowerSequenceGenerator.generate_sequence(term_count)
    
    for i, value in enumerate(sequence):
        print(f" -> 2 raised to power {i:2}: {value:6}")
        
    print("-" * 40)

if __name__ == "__main__":
    run_power_demo()
