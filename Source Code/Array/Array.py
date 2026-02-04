"""
File: Array.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    This script implements a custom Static Array structure in Python. 
    Unlike Python's built-in dynamically-sized lists, this Array has 
    a fixed capacity defined at creation, simulating low-level memory 
    allocation behaviors. It includes methods for insertion, deletion, 
    and searching with strict bounds checking.

Complexity Analysis:
    - Access/Update (by index): O(1)
    - Insertion (any position): O(N) due to element shifting.
    - Deletion: O(N) due to shifting (compacting) or searching.
    - Search: O(N) linear search.
    - Space Complexity: O(Capacity) to pre-allocate storage.

Logic:
    1. Initialize internal storage with a fixed size and optional default values.
    2. Maintain a count of "active" elements independently of the capacity.
    3. Shift elements forward/backward during insertion/deletion to maintain 
       contiguous memory simulation.
    4. Raise appropriate exceptions (IndexError, ValueError) for invalid operations.
"""

from typing import Any, List, Optional, TypeVar, Generic

T = TypeVar('T')

class ArrayError(Exception):
    """Custom exception for Array structure operations."""
    pass

class Array(Generic[T]):
    """
    A fixed-capacity array implementation.
    """
    def __init__(self, capacity: int, initial_elements: Optional[List[T]] = None):
        """
        Initializes the Array with a fixed capacity.

        Args:
            capacity (int): The maximum number of elements the array can hold.
            initial_elements (Optional[List[T]]): List of elements to pre-fill.

        Raises:
            ArrayError: If capacity is not a positive integer or initial_elements exceeds capacity.
        """
        if not isinstance(capacity, int) or capacity <= 0:
            raise ArrayError("Array capacity must be a positive integer.")
        
        self._capacity = capacity
        self._items: List[Optional[T]] = [None] * capacity
        self._count = 0

        if initial_elements:
            if len(initial_elements) > capacity:
                raise ArrayError("Initial elements exceed specified capacity.")
            for i, val in enumerate(initial_elements):
                self._items[i] = val
            self._count = len(initial_elements)

    @property
    def capacity(self) -> int:
        """Returns the total capacity of the array."""
        return self._capacity

    def __len__(self) -> int:
        """Returns the number of active elements in the array."""
        return self._count

    def __getitem__(self, index: int) -> T:
        """Gets the element at the specified index."""
        if not 0 <= index < self._count:
            raise IndexError("Array index out of range")
        return self._items[index] # type: ignore

    def __setitem__(self, index: int, value: T) -> None:
        """Sets the element at the specified index."""
        if not 0 <= index < self._count:
            raise IndexError("Array index out of range")
        self._items[index] = value

    def insert_at(self, index: int, element: T) -> None:
        """
        Inserts an element at a specific index, shifting subsequent elements.

        Args:
            index (int): The position to insert at.
            element (T): The value to insert.

        Raises:
            IndexError: If the index is out of bounds [0, count].
            ArrayError: If the array is full.
        """
        if self._count >= self._capacity:
            raise ArrayError("Cannot insert: Array is at full capacity.")
        
        if not 0 <= index <= self._count:
            raise IndexError("Insertion index out of range.")

        # Shift elements to the right
        for i in range(self._count, index, -1):
            self._items[i] = self._items[i - 1]
        
        self._items[index] = element
        self._count += 1

    def append(self, element: T) -> None:
        """Appends an element to the end of the active array."""
        self.insert_at(self._count, element)

    def delete_at(self, index: int) -> T:
        """
        Deletes the element at the specified index and shifts others to close the gap.

        Args:
            index (int): The position of the element to remove.

        Returns:
            T: The removed element.

        Raises:
            IndexError: If index is out of bounds.
        """
        if not 0 <= index < self._count:
            raise IndexError("Deletion index out of range.")
        
        removed_item = self._items[index]
        
        # Shift elements to the left
        for i in range(index, self._count - 1):
            self._items[i] = self._items[i + 1]
            
        self._items[self._count - 1] = None
        self._count -= 1
        return removed_item # type: ignore

    def search(self, element: T) -> int:
        """
        Searches for the first occurrence of an element.

        Args:
            element (T): The value to find.

        Returns:
            int: The index of the element.

        Raises:
            ValueError: If the element is not found.
        """
        for i in range(self._count):
            if self._items[i] == element:
                return i
        raise ValueError(f"Element '{element}' not found in Array.")

    def __repr__(self) -> str:
        """Returns a string representation of the active elements."""
        active_items = [self._items[i] for i in range(self._count)]
        return f"Array(count={self._count}, capacity={self._capacity}, items={active_items})"

def run_array_demo() -> None:
    """Demonstrates standard Array operations."""
    print("--- Python Shorts: Custom Array Implementation Demo ---")
    try:
        # Initialize with capacity 5 and one element
        arr = Array(5, [10])
        print(f"Initial: {arr}")
        
        arr.insert_at(0, 5)   # Insert at start
        print(f"After insert_at(0, 5): {arr}")
        
        arr.append(20)        # Append at end
        print(f"After append(20): {arr}")
        
        arr.insert_at(1, 7)   # Insert in middle
        print(f"After insert_at(1, 7): {arr}")
        
        idx = arr.search(20)
        print(f"Search for 20: Found at index {idx}")
        
        removed = arr.delete_at(2)
        print(f"Delete at index 2 (val {removed}): {arr}")
        
    except (ArrayError, IndexError, ValueError) as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    run_array_demo()
