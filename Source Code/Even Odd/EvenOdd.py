"""
File: EvenOdd.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    A high-fidelity implementation for partitioning collections of integers 
    based on their parity. This module provides optimized mechanisms for 
    segregating even and odd integers, suitable for discrete mathematical 
    analysis and algorithmic processing.

Mathematical Logic:
    Parity is the property of an integer's membership in one of two disjoint 
    sets: Even (2k) or Odd (2k + 1). This implementation uses Euclid's Division 
    Lemma to determine the remainder r in n = 2q + r.
"""

from typing import List, Dict, Tuple

class CollectionError(Exception):
    """Exception raised for invalid collection elements."""
    pass

def partition_even_odd(nums: List[int]) -> Dict[str, List[int]]:
    """
    Categorizes a collection of integers into Even and Odd subsets.

    Args:
        nums (List[int]): A sequence of integers to be partitioned.

    Returns:
        Dict[str, List[int]]: A dictionary containing 'even' and 'odd' keys 
                              mapped to their respective integer collections.

    Raises:
        CollectionError: If any element in the collection is not an integer.
    """
    partitioned = {'even': [], 'odd': []}
    
    for n in nums:
        # Robust type verification
        if not isinstance(n, int):
            raise CollectionError(f"Invalid element: {n}. All elements must be integers.")
            
        # Parity detection via modular arithmetic
        if n % 2 == 0:
            partitioned['even'].append(n)
        else:
            partitioned['odd'].append(n)
            
    return partitioned

def run_partition_demo():
    """Execution demo with structured integer collections."""
    print("--- Python Shorts: Discrete Parity Partitioning (Even/Odd) ---")
    
    collections = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [101, 202, 303, 404, 505],
        [0, -1, -2, -3, -4]
    ]
    
    for i, data in enumerate(collections, 1):
        print(f"\n[Dataset {i}]: {data}")
        result = partition_even_odd(data)
        print(f"[Result]: Even={result['even']} | Odd={result['odd']}")

    # Error handling demonstration
    print("\n[Robustness Check]: Attempting to partition heterogeneous list [1, '2', 3]")
    try:
        partition_even_odd([1, "2", 3]) # type: ignore
    except CollectionError as e:
        print(f"[Captured Error]: {e}")

if __name__ == "__main__":
    run_partition_demo()
