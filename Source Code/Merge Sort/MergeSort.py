"""
File: MergeSort.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    A high-fidelity implementation of the Merge Sort algorithm. This module 
    leverages the Divide and Conquer paradigm to achieve stable, guaranteed 
    O(n log n) sorting complexity.

Mathematical Logic:
    Merge Sort recursively partitions a dataset into atomic sub-problems, 
    solves them, and merges the results in linear time. The recurrence 
    relation is T(n) = 2T(n/2) + O(n), which resolves to O(n log n) via the 
    Master Theorem.
"""

from typing import List, Any

class MergeSorter:
    """Scholarly implementation of the Merge Sort algorithm."""
    
    @staticmethod
    def sort(dataset: List[Any]) -> List[Any]:
        """
        Sorts a dataset using the Merge Sort algorithm.

        Args:
            dataset (List[Any]): The list of elements to be sorted.

        Returns:
            List[Any]: A new list containing the sorted elements.
        """
        if len(dataset) <= 1:
            return dataset

        # Divide and Conquer
        middle = len(dataset) // 2
        left_half = MergeSorter.sort(dataset[:middle])
        right_half = MergeSorter.sort(dataset[middle:])

        return MergeSorter._merge(left_half, right_half)

    @staticmethod
    def _merge(left: List[Any], right: List[Any]) -> List[Any]:
        """
        Merges two sorted sub-arrays into a single sorted array.
        Uses index pointers for O(n) efficiency.
        """
        merged = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        # Append remaining elements
        merged.extend(left[i:])
        merged.extend(right[j:])
        
        return merged

def run_sorting_demo():
    """Execution demo with diverse test vectors."""
    print("--- Python Shorts: Merge Sort (Stable Divide & Conquer) ---")
    
    test_vectors = [
        [3, 4, 2, 6, 5, 7, 1, 9],
        [10, -1, 5, 2, 0, 8],
        [1],
        [],
        [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    ]

    for vector in test_vectors:
        print(f"[Input]:  {vector}")
        sorted_vector = MergeSorter.sort(vector)
        print(f" -> Result: {sorted_vector}\n")

if __name__ == "__main__":
    run_sorting_demo()
