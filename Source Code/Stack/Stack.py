"""
File: Stack.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    This module implements a bounded Stack data structure using list-based 
    storage. It demonstrates the Last-In-First-Out (LIFO) principle, supporting 
    fundamental operations like push, pop, peek, and capacity management with 
    overflow/underflow detection.

Complexity Analysis:
    - Time Complexity:
        - Push: O(1) amortized 
        - Pop: O(1)
        - Peek: O(1)
        - isEmpty/isFull: O(1)
    - Space Complexity: O(n) where n is the capacity.

Logic:
    1. Initialize a stack with a fixed maximum capacity.
    2. Push: Add elements to the top if not full.
    3. Pop: Remove and return the top element if not empty.
    4. Peek: View the top element without removal.
    5. Track size and enforce capacity constraints.
"""

from typing import Any, Optional, List


class StackService:
    """
    A service class implementing a bounded LIFO stack.
    """

    def __init__(self, capacity: int):
        """
        Initializes a stack with specified capacity.
        
        Args:
            capacity: Maximum number of elements the stack can hold.
        """
        self.capacity = capacity
        self.items: List[Any] = []

    def __str__(self) -> str:
        """String representation of the stack."""
        return ' '.join(str(item) for item in self.items)

    def push(self, data: Any) -> bool:
        """
        Pushes an element onto the top of the stack.
        
        Args:
            data: The element to push.
            
        Returns:
            True if successful, False if stack is full.
        """
        if not self.is_full():
            self.items.append(data)
            return True
        else:
            print('Stack Overflow: Cannot push, stack is full.')
            return False

    def pop(self) -> Optional[Any]:
        """
        Removes and returns the top element.
        
        Returns:
            The top element, or None if stack is empty.
        """
        if not self.is_empty():
            return self.items.pop()
        else:
            print('Stack Underflow: Cannot pop, stack is empty.')
            return None

    def peek(self) -> Optional[Any]:
        """
        Returns the top element without removing it.
        
        Returns:
            The top element, or None if stack is empty.
        """
        if not self.is_empty():
            return self.items[-1]
        else:
            print('Stack is empty.')
            return None

    def is_empty(self) -> bool:
        """Checks if the stack is empty."""
        return len(self.items) == 0

    def is_full(self) -> bool:
        """Checks if the stack has reached capacity."""
        return len(self.items) == self.capacity

    def size(self) -> int:
        """Returns the current number of elements in the stack."""
        return len(self.items)


def main():
    """
    Demonstrates the scholarly Stack implementation.
    """
    print("--- Stack Service Demo ---")
    
    stack = StackService(capacity=10)
    
    print(f"Pushing elements 0-9...")
    for i in range(10):
        stack.push(i)
    
    print(f"Is Empty? {stack.is_empty()}")
    print(f"Is Full? {stack.is_full()}")
    print(f"Stack Contents: {stack}")
    print(f"Stack Size: {stack.size()}")
    
    popped = stack.pop()
    print(f"Popped Element: {popped}")
    print(f"Stack After Pop: {stack}")
    
    top = stack.peek()
    print(f"Top Element (Peek): {top}")
    print(f"Stack Size: {stack.size()}")
    
    print("\nDemo Complete.")


if __name__ == "__main__":
    main()
