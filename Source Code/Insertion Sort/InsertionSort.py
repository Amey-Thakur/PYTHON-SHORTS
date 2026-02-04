"""
File: InsertionSort.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    A high-fidelity implementation of the Insertion Sort algorithm. This module 
    demonstrates an incremental approach to sorting, where an array is split 
    into sorted and unsorted partitions. Elements are iteratively 'inserted' 
    into their correct position within the sorted section.

Mathematical Logic:
    Insertion Sort is an O(n^2) algorithm that maintains a loop invariant: 
    at the start of each iteration i, the sub-array A[0...i-1] is sorted. 
    It is particularly efficient for datasets with low inversion counts 
    or small cardinality.
"""

from typing import List, Any

class InsertionSorter:
    """Scholarly implementation of the Insertion Sort algorithm."""
    
    @staticmethod
    def sort(dataset: List[Any]) -> List[Any]:
        """
        Performs an in-place insertion sort of the provided dataset.

        Args:
            dataset (List[Any]): The list of comparable elements to sort.

        Returns:
            List[Any]: The sorted list (modified in-place).
        """
        n = len(dataset)
        if n <= 1:
            return dataset

        # Iterate from the first element (index 1) to the end
        for i in range(1, n):
            key = dataset[i]
            # Move elements of dataset[0..i-1] that are greater than key
            # to one position ahead of their current position
            j = i - 1
            while j >= 0 and dataset[j] > key:
                dataset[j + 1] = dataset[j]
                j -= 1
            dataset[j + 1] = key
            
        return dataset

def run_sort_demo():
    """Execution demo with heterogeneous and boundary test vectors."""
    print("--- Python Shorts: Insertion Sort & Incremental Logic ---")
    
    test_cases = {
        "Unsorted": [3, 4, 2, 6, 5, 7, 1, 9],
        "Nearly Sorted": [1, 2, 3, 5, 4, 6],
        "Redundant": [5, 2, 5, 1, 2],
        "Negative": [0, -5, 10, -2, 3]
    }

    for name, data in test_cases.items():
        print(f"\n[Dataset: {name}]")
        print(f" Original: {data}")
        sorted_data = InsertionSorter.sort(list(data))
        print(f" Sorted:   {sorted_data}")

if __name__ == "__main__":
    run_sort_demo()
