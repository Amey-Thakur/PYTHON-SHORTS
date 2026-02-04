"""
File: NarySearch.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    A high-fidelity implementation of N-ary Search, a generalization of Binary 
    Search that partitions the search space into N sub-intervals. This module 
    leverages Divide and Conquer strategies to achieve O(log_n N) complexity.

Mathematical Logic:
    In N-ary search, a sorted dataset is divided into n equal parts using n-1 
    pivots. The algorithm identifies which sub-interval the search key belongs 
    to and recursively narrows the search space.
    The recurrence relation is T(N) = T(N/n) + O(n).
"""

from typing import List, Optional

class NarySearchEngine:
    """Scholarly implementation of N-ary Search algorithms."""

    @staticmethod
    def search(dataset: List[int], key: int, partitions: int = 10) -> Optional[int]:
        """
        Performs an N-ary search on a sorted list.

        Args:
            dataset (List[int]): The sorted list of integers.
            key (int): The value to search for.
            partitions (int): The number of divisions (n) per iteration.

        Returns:
            Optional[int]: The index of the key if found, else None.
        """
        if not dataset:
            return None
            
        return NarySearchEngine._recursive_search(dataset, key, 0, len(dataset) - 1, partitions)

    @staticmethod
    def _recursive_search(dataset: List[int], key: int, low: int, high: int, n: int) -> Optional[int]:
        """Internal recursive helper for N-ary partitioning."""
        if low > high:
            return None

        # Boundary checks
        if key < dataset[low] or key > dataset[high]:
            return None
        
        if key == dataset[low]:
            return low
        if key == dataset[high]:
            return high

        # Size of the current search interval
        size = high - low + 1
        if size <= n:
            # Fallback to linear search for very small intervals
            for i in range(low, high + 1):
                if dataset[i] == key:
                    return i
            return None

        # Calculate n-1 pivots
        step = size // n
        pivots = []
        for i in range(1, n):
            pivots.append(low + i * step)

        # Check pivots and identify sub-interval
        if key < dataset[pivots[0]]:
            return NarySearchEngine._recursive_search(dataset, key, low + 1, pivots[0] - 1, n)
            
        for i in range(len(pivots) - 1):
            if key == dataset[pivots[i]]:
                return pivots[i]
            if dataset[pivots[i]] < key < dataset[pivots[i+1]]:
                return NarySearchEngine._recursive_search(dataset, key, pivots[i] + 1, pivots[i+1] - 1, n)

        if key == dataset[pivots[-1]]:
            return pivots[-1]
            
        if key > dataset[pivots[-1]]:
            return NarySearchEngine._recursive_search(dataset, key, pivots[-1] + 1, high - 1, n)

        return None

def run_search_demo():
    """Execution demo with large numerical search spaces."""
    print("--- Python Shorts: N-ary Search Computational Service ---")
    
    # Generate a large sorted dataset
    ARRAY_SIZE = 1000
    dataset = list(range(ARRAY_SIZE + 1))
    
    test_keys = [433, 7, 999, 1001, -5, 500]
    n_partitions = 10

    for key in test_keys:
        print(f"[Searching]: Key = {key} with {n_partitions}-ary partitions")
        index = NarySearchEngine.search(dataset, key, n_partitions)
        
        if index is not None:
            print(f" -> Status: Element Found at index {index}\n")
        else:
            print(f" -> Status: Element Not Found (Out of Range or Missing)\n")

if __name__ == "__main__":
    run_search_demo()
