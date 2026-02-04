"""
File: OddNumberGenerator.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    A high-fidelity computational utility for generating odd number sequences. 
    This module utilizes Python's generator protocol for lazy evaluation, 
    efficiently yielding terms of an arithmetic progression where the common 
    difference is 2.

Mathematical Logic:
    An odd number is defined as an integer of the form n = 2k + 1, where 
    k is an integer. The sequence of positive odd numbers is an arithmetic 
    progression with initial term a_1 = 1 and common difference d = 2.
"""

from typing import Iterator, List

class OddNumberCalculator:
    """Scholarly implementation of odd number generation services."""
    
    @staticmethod
    def generate_infinite() -> Iterator[int]:
        """
        Creates an infinite generator for the odd number series.

        Yields:
            int: The next odd number in the sequence {1, 3, 5, ...}.
        """
        n = 1
        while True:
            yield n
            n += 2

    @staticmethod
    def get_sequence(count: int) -> List[int]:
        """
        Computes a finite sequence of the first 'count' odd numbers.

        Args:
            count (int): The number of odd integers to retrieve.

        Returns:
            List[int]: The list of generated odd numbers.
        """
        if count < 0:
            return []
            
        generator = OddNumberCalculator.generate_infinite()
        return [next(generator) for _ in range(count)]

def run_generator_demo():
    """Execution demo showcasing lazy evaluation of arithmetic sequences."""
    print("--- Python Shorts: Odd Number Generation Service ---")
    
    # Bounded sequence generation
    limit = 10
    print(f"[Input]: Requesting first {limit} odd integers")
    sequence = OddNumberCalculator.get_sequence(limit)
    print(f" -> Resulting Sequence: {sequence}\n")

    # Dynamic generation retrieval
    print("[Input]: Manual iteration of infinite generator")
    gen = OddNumberCalculator.generate_infinite()
    vals = [next(gen) for _ in range(5)]
    print(f" -> Next 5 Values: {vals}")

if __name__ == "__main__":
    run_generator_demo()
