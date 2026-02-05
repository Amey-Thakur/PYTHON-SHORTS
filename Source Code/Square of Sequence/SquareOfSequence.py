"""
File: SquareOfSequence.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    This module implements a generator-based square sequence utility. It 
    demonstrates the use of Python generators for lazy evaluation, allowing
    for memory-efficient generation of quadratic sequences where each element
    is the square of its index within the sequence.

Complexity Analysis:
    - Time Complexity: O(1) for each element generated (amortized).
    - Space Complexity: O(1) auxiliary space beyond the yielded value.

Logic:
    1. Define a generator function that iterates from 0 up to a specified limit.
    2. Within the iteration, yield the square of the current index.
    3. Encapsulate the generator logic within a service class for structured access.
    4. Provide a demo method that consumes the generator and prints the sequence.
"""

from typing import Generator


class SequenceGeneratorService:
    """
    A service class for producing mathematical sequences using lazy evaluation.
    """

    @staticmethod
    def square_of_sequence(limit: int) -> Generator[int, None, None]:
        """
        Generates a sequence of square numbers up to a specified count.
        
        Args:
            limit: The number of elements to generate in the sequence.
            
        Yields:
            The square of the current index (i * i).
        """
        for i in range(limit):
            yield i * i


def main():
    """
    Demonstrates the scholarly Square of Sequence generator implementation.
    """
    print("--- Square of Sequence Service Demo ---")
    
    try:
        limit_str = input("Enter Sequence Limit: ")
        limit = int(limit_str) if limit_str.strip() else 10
    except ValueError:
        print("Invalid input. Defaulting to 10 iterations.")
        limit = 10

    service = SequenceGeneratorService()
    generator = service.square_of_sequence(limit)

    print(f"Generating first {limit} square numbers:")
    
    count = 0
    while True:
        try:
            square = next(generator)
            print(f"Index {count}: {square}")
            count += 1
        except StopIteration:
            break

    print("\nSequence Generation: Successfully Terminated.")


if __name__ == "__main__":
    main()
