"""
File: HeapSort.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    A high-fidelity implementation of the Heap Sort algorithm. This module 
    leverages the properties of a Complete Binary Tree (Max-Heap) to sort 
    elements in-place with optimal asymptotic complexity.

Mathematical Logic:
    Heap Sort operates by transforming an unsorted array into a Max-Heap structure. 
    In a Max-Heap, for every node i, A[parent(i)] >= A[i]. The algorithm 
    repeatedly extracts the maximum element and restores the heap property, 
    achieving a total order in O(n log n) time.
"""

from typing import List, Any

class HeapSorter:
    """Scholarly implementation of the Heap Sort algorithm using a Max-Heap structure."""
    
    @staticmethod
    def sort(dataset: List[Any]) -> List[Any]:
        """
        Performs an in-place sort of the provided dataset.

        Args:
            dataset (List[Any]): The list of comparable elements to sort.

        Returns:
            List[Any]: The sorted list (modified in-place).
        """
        n = len(dataset)
        if n <= 1:
            return dataset

        # Phase 1: Build Max-Heap (Heapify)
        # Starting from the last non-leaf node down to the root
        for i in range(n // 2 - 1, -1, -1):
            HeapSorter._sift_down(dataset, n, i)

        # Phase 2: Extract elements from heap one by one
        for i in range(n - 1, 0, -1):
            # Move current root (maximum) to the end
            dataset[i], dataset[0] = dataset[0], dataset[i]
            # Restore heap property on the reduced set
            HeapSorter._sift_down(dataset, i, 0)
        
        return dataset

    @staticmethod
    def _sift_down(arr: List[Any], n: int, i: int):
        """Restores the max-heap property for a subtree rooted at index i."""
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        # Check if left child exists and is greater than root
        if left < n and arr[left] > arr[largest]:
            largest = left

        # Check if right child exists and is greater than current largest
        if right < n and arr[right] > arr[largest]:
            largest = right

        # If largest is not root, swap and continue sifting down
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            HeapSorter._sift_down(arr, n, largest)

def run_sort_demo():
    """Execution demo with heterogeneous and boundary test vectors."""
    print("--- Python Shorts: Heap Sort & Binary Heaps ---")
    
    test_cases = {
        "Standard": [12, 11, 13, 5, 6, 7],
        "Redundant": [3, 1, 4, 1, 5, 9, 2, 6, 5],
        "Reversed": [10, 8, 6, 4, 2, 0],
        "Negative": [0, -5, 2, -10, 15]
    }

    for name, data in test_cases.items():
        print(f"\n[Dataset: {name}]")
        print(f" Original: {data}")
        sorted_data = HeapSorter.sort(list(data))
        print(f" Sorted:   {sorted_data}")

if __name__ == "__main__":
    run_sort_demo()
