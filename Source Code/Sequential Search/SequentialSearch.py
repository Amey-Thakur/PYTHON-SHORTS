"""
File: SequentialSearch.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    This module implements the Sequential Search (Linear Search) algorithm, 
    an exhaustive scan utility for identifying a target element within an 
    unordered collection. It utilizes early exit optimization to minimize 
    redundant comparisons.

Complexity Analysis:
    - Time Complexity: O(n), where n is the number of elements in the collection.
      - Best Case: O(1) if the target is at the first position.
      - Worst Case: O(n) if the target is at the final position or absent.
    - Space Complexity: O(1) auxiliary space, as it requires only a single 
      pointer for iteration.

Logic:
    1. Initialize a pointer (index) at the start of the sequence.
    2. Iterate through each element sequentially.
    3. Compare the current element with the target value.
    4. If a match is found, immediately return the current index (Early Exit).
    5. If the end of the sequence is reached without a match, return -1.
    6. Ensure the service handles diverse data types through Python's 
       generic equality comparisons.
"""

from typing import Any, List, Optional


class SequentialSearchService:
    """
    A service class for executing Sequential Search algorithmic logic.
    """

    @staticmethod
    def find(target: Any, collection: List[Any]) -> Optional[int]:
        """
        Identifies the position of a target element using linear search.
        
        Args:
            target: The value to search for.
            collection: The list to search through.
            
        Returns:
            The zero-based index of the first occurrence if found, else -1.
        """
        for index, item in enumerate(collection):
            if item == target:
                return index
        return -1


def main():
    """
    Demonstrates the scholarly Sequential Search implementation.
    """
    print("--- Sequential Search Service Demo ---")
    
    # Demonstration dataset
    target_data = [10, 23, 45, 70, 11, 15]
    search_value = 70
    
    print(f"Collection: {target_data}")
    print(f"Targeting:  {search_value}")
    
    service = SequentialSearchService()
    result_index = service.find(search_value, target_data)
    
    if result_index != -1:
        print(f"\nTarget Found: Index {result_index}")
    else:
        print("\nTarget Not Found in Collection")


if __name__ == "__main__":
    main()
