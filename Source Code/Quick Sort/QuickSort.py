"""
File: QuickSort.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    A high-fidelity implementation of the Quick Sort algorithm. This module 
    leverages the 'Divide and Conquer' paradigm to sort data in-place, 
    utilizing Hoare partitioning for optimized memory usage and performance.

Mathematical Logic:
    Quick Sort operates by selecting a 'pivot' and partitioning the array 
    into two sub-arrays according to whether elements are less than or 
    greater than the pivot. The average-case time complexity is O(n log n).
"""

import time
from typing import List

class QuickSortService:
    """Scholarly implementation of the Quick Sort sorting algorithm."""

    def sort(self, data: List[int]) -> List[int]:
        """
        Public interface for the Quick Sort operation.

        Args:
            data (List[int]): The list of integers to be sorted.

        Returns:
            List[int]: The sorted list.
        """
        if not data:
            return []
        
        self._quick_sort(data, 0, len(data) - 1)
        return data

    def _quick_sort(self, arr: List[int], low: int, high: int):
        """Recursive sorting orchestrator."""
        if low < high:
            # Partition the array and retrieve the pivot index
            pivot_index = self._partition(arr, low, high)
            
            # Recursively sort the sub-arrays
            self._quick_sort(arr, low, pivot_index)
            self._quick_sort(arr, pivot_index + 1, high)

    def _partition(self, arr: List[int], low: int, high: int) -> int:
        """Hoare Partitioning Scheme implementation."""
        pivot = arr[(low + high) // 2]
        i = low - 1
        j = high + 1
        
        while True:
            i += 1
            while arr[i] < pivot:
                i += 1
                
            j -= 1
            while arr[j] > pivot:
                j -= 1
                
            if i >= j:
                return j
            
            # Swap elements at indices i and j
            arr[i], arr[j] = arr[j], arr[i]

def run_sorting_demo():
    """Execution demo showcasing sorting performance and correctness."""
    print("--- Python Shorts: Quick Sort Verification Service ---")
    
    # Test vector
    sample_list = [3, 4, 2, 6, 5, 7, 1, 9]
    print(f"[Input]:  {sample_list}")
    
    service = QuickSortService()
    
    start_time = time.time()
    sorted_result = service.sort(sample_list.copy())
    end_time = time.time()
    
    print(f" -> Result: {sorted_result}")
    print(f"Execution Analytics: {end_time - start_time:.6f} seconds")

if __name__ == "__main__":
    run_sorting_demo()
