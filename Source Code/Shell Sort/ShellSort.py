"""
File: ShellSort.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    This module implements the Shell Sort algorithm, an in-place comparison 
    sort that generalizes insertion sort by allowing the exchange of items 
    that are far apart. It utilizes a diminishing increment gap sequence 
    to progressively improve the partial ordering of the collection.

Complexity Analysis:
    - Time Complexity: O(n log^2 n) to O(n^{3/2}) depending on the gap sequence.
      - Best Case: O(n log n).
      - Worst Case: O(n^2) with the standard Shell's sequence (N/2^k).
    - Space Complexity: O(1) auxiliary space.

Logic:
    1. Define an initial gap size (typically n/2).
    2. Divide the list into sub-lists based on the gap increment.
    3. Perform a gapped insertion sort on each sub-list.
    4. Reduce the gap (diminishing increment) and repeat the process.
    5. Terminate when the gap reaches 1, concluding with a final insertion sort.
    6. This approach minimizes the total number of swaps by moving elements 
       toward their final positions more rapidly than nearest-neighbor sorts.
"""

from typing import List


class ShellSortService:
    """
    A service class for executing Shell Sort algorithmic logic.
    """

    @staticmethod
    def sort(data: List[int]) -> List[int]:
        """
        Sorts a list of integers using the Shell Sort algorithm.
        
        Args:
            data: A mutable list of integers to be sorted.
            
        Returns:
            The same list, sorted in ascending order.
        """
        n = len(data)
        gap = n // 2
        
        # Iteratively reduce the gap size
        while gap > 0:
            # Perform gapped insertion sort for each sub-sequence
            for i in range(gap, n):
                current_value = data[i]
                j = i
                
                # Shift elements of the gapped sub-sequence until the target 
                # position is identified
                while j >= gap and data[j - gap] > current_value:
                    data[j] = data[j - gap]
                    j -= gap
                
                # Insert the value into its relatively sorted position
                data[j] = current_value
            
            # Reduce gap using the standard N/2 progression
            gap //= 2
            
        return data


def main():
    """
    Demonstrates the scholarly Shell Sort implementation.
    """
    print("--- Shell Sort Service Demo ---")
    
    # Demonstration dataset
    target_list = [12, 23, 4, 5, 3, 2, 12, 81, 56, 95]
    
    print(f"Original Sequence: {target_list}")
    
    sorter = ShellSortService()
    sorted_result = sorter.sort(target_list)
    
    print(f"Sorted Sequence:   {sorted_result}")


if __name__ == "__main__":
    main()
