"""
File: SelectionSort.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    This module implements the Selection Sort algorithm, an in-place comparison 
    sorting utility. It utilizes a minimum selection paradigm to iteratively 
    organize elements, ensuring optimal space complexity for small datasets.

Complexity Analysis:
    - Time Complexity: O(n^2), where n is the number of elements (Best, Average, 
      and Worst cases).
    - Space Complexity: O(1) auxiliary space, as it performs in-place swaps.

Logic:
    1. Iterate through the entire list from index 0 to n-1.
    2. For each position i, perform a linear search to find the minimum element 
       in the sub-list [i, n].
    3. Swap the found minimum element with the element at the current position i.
    4. Repeat the process until the entire sequence is sorted in ascending order.
    5. Ensure the implementation remains in-place to minimize memory overhead.
"""

from typing import List


class SelectionSortService:
    """
    A service class for executing Selection Sort algorithmic logic.
    """

    @staticmethod
    def sort(data: List[int]) -> List[int]:
        """
        Sorts a list of integers using the Selection Sort algorithm.
        
        Args:
            data: A mutable list of integers to be sorted.
            
        Returns:
            The same list, sorted in ascending order.
        """
        n = len(data)
        for i in range(n - 1):
            # Assume the current position is the minimum
            min_index = i
            
            # Identify the actual minimum in the remaining unsorted portion
            for j in range(i + 1, n):
                if data[j] < data[min_index]:
                    min_index = j
            
            # Perform an in-place swap if a smaller element was found
            if min_index != i:
                data[i], data[min_index] = data[min_index], data[i]
        
        return data


def main():
    """
    Demonstrates the scholarly Selection Sort implementation.
    """
    print("--- Selection Sort Service Demo ---")
    
    # Demonstration dataset
    target_list = [64, 25, 12, 22, 11, 90, 1]
    
    print(f"\nOriginal Sequence: {target_list}")
    
    sorter = SelectionSortService()
    sorted_list = sorter.sort(target_list)
    
    print(f"Sorted Sequence:   {sorted_list}")


if __name__ == "__main__":
    main()
