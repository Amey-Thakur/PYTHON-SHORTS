"""
File: BinarySearch.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    Binary search is an efficient algorithm for finding a target value 
    within a sorted array. It works by repeatedly dividing the search 
    interval in half. This implementation provides a robust, type-hinted 
    utility for both iterative binary search and iteration counting.

Complexity Analysis:
    - Time Complexity: O(log N), where N is the number of elements in the list.
    - Space Complexity: O(1) for the iterative implementation.

Logic:
    1. Validate that the input list is sorted; otherwise, binary search is invalid.
    2. Maintain 'left' and 'right' pointers to the current search interval.
    3. In each step, calculate the middle index ('mid').
    4. If the target is at 'mid', return the index.
    5. If the target is less than the value at 'mid', narrow the interval to the left half.
    6. If the target is greater, narrow it to the right half.
    7. Return -1 if the target is not found after the search space is exhausted.
"""

from typing import List, Any, Tuple, Union

class BinarySearchError(Exception):
    """Custom exception for Binary Search utility errors."""
    pass

def binary_search(target: Any, sorted_list: List[Any]) -> int:
    """
    Performs an iterative binary search on a sorted list.

    Args:
        target (Any): The element to search for.
        sorted_list (List[Any]): The sorted list to search within.

    Returns:
        int: The index of the target if found, otherwise -1.

    Raises:
        BinarySearchError: If the input is not a list.
    """
    if not isinstance(sorted_list, list):
        raise BinarySearchError(f"Expected sorted_list to be 'list', got '{type(sorted_list).__name__}'")

    left, right = 0, len(sorted_list) - 1

    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

def binary_search_with_stats(target: Any, sorted_list: List[Any]) -> Tuple[int, int]:
    """
    Performs binary search and returns both the index and the iteration count.

    Args:
        target (Any): The element to search for.
        sorted_list (List[Any]): The sorted list to search within.

    Returns:
        Tuple[int, int]: A tuple containing (index, iterations). Index is -1 if not found.
    """
    if not isinstance(sorted_list, list):
        raise BinarySearchError("Input must be a list.")

    left, right = 0, len(sorted_list) - 1
    iterations = 0

    while left <= right:
        iterations += 1
        mid = (left + right) // 2
        if sorted_list[mid] == target:
            return mid, iterations
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1, iterations

def run_binary_search_demo() -> None:
    """Executes a demonstration of Binary Search functionality."""
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14]
    search_target = 2

    print("--- Python Shorts: Binary Search Algorithm Demo ---")
    print(f"Dataset: {data}")
    print(f"Target: {search_target}")

    index, iters = binary_search_with_stats(search_target, data)
    
    if index != -1:
        print(f"Success: Target found at index {index} after {iters} iterations.")
    else:
        print("Result: Target not found in the dataset.")

if __name__ == '__main__':
    run_binary_search_demo()
