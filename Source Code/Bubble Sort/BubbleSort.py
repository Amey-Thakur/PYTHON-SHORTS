"""
File: BubbleSort.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    Bubble Sort is a simple comparison-based sorting algorithm. It 
    repeatedly steps through the list, compares adjacent elements, and 
    swaps them if they are in the wrong order. This implementation 
    includes an optimization to terminate early if the list is already sorted.

Complexity Analysis:
    - Time Complexity: O(N^2) worst/average case; O(N) best case (with optimization).
    - Space Complexity: O(1) in-place sorting.

Logic:
    1. Iterate through the list N times.
    2. In each pass, compare adjacent elements.
    3. If the left element > right element, swap them.
    4. Track if any swap occurred during the pass.
    5. If no swaps occurred, the list is sorted; exit early.
"""

from typing import List, Any

def bubble_sort(arr: List[Any]) -> List[Any]:
    """
    Sorts a list using the optimized Bubble Sort algorithm.

    Args:
        arr (List[Any]): The list to be sorted.

    Returns:
        List[Any]: The sorted list (modified in-place, but returned for convenience).
    """
    n = len(arr)
    for i in range(n):
        swapped = False
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no two elements were swapped by inner loop, then break
        if not swapped:
            break
            
    return arr

def run_bubble_sort_demo() -> None:
    """Demonstrates Bubble Sort."""
    print("--- Python Shorts: Bubble Sort Optimization Demo ---")
    data = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original: {data}")
    sorted_data = bubble_sort(data.copy())
    print(f"Sorted  : {sorted_data}")

if __name__ == '__main__':
    run_bubble_sort_demo()
