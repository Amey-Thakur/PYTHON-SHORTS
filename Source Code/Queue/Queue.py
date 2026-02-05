"""
File: Queue.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    A high-performance implementation of the Queue abstract data type. 
    This module utilizes 'collections.deque' to ensure O(1) time 
    complexity for both enqueue and dequeue operations, adhering to 
    the First-In, First-Out (FIFO) principle.

Mathematical Logic:
    A queue is a linear collection of entities that are maintained in 
    a sequence and can be modified by the addition of entities at one 
    end (rear) and removal of entities from the other end (front).
"""

from collections import deque
from typing import Any, Optional

class QueueService:
    """Scholarly implementation of a high-performance FIFO sequence."""

    def __init__(self, capacity: Optional[int] = None):
        """
        Initializes the queue with an optional fixed capacity.

        Args:
            capacity (Optional[int]): Max size of the queue. If None, size is unbounded.
        """
        self._container = deque(maxlen=capacity)
        self._capacity = capacity

    def enqueue(self, item: Any) -> bool:
        """
        Adds an item to the rear of the queue.

        Args:
            item (Any): The element to be enqueued.

        Returns:
            bool: True if successful, False if the queue is at capacity.
        """
        if self.is_full():
            print("[Warning]: Queue is at capacity. Enqueue operation failed.")
            return False
        
        self._container.append(item)
        return True

    def dequeue(self) -> Any:
        """
        Removes and returns the item from the front of the queue.

        Returns:
            Any: The dequeued element.

        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            print("[Warning]: Attempted to dequeue from an empty container.")
            raise IndexError("Dequeue from empty queue")
        
        return self._container.popleft()

    def peek(self) -> Any:
        """
        Returns the front element without removing it.

        Returns:
            Any: The front element.
        """
        if self.is_empty():
            return None
        return self._container[0]

    def is_empty(self) -> bool:
        """Checks if the queue contains no elements."""
        return len(self._container) == 0

    def is_full(self) -> bool:
        """Checks if the queue has reached its designated capacity."""
        if self._capacity is None:
            return False
        return len(self._container) == self._capacity

    def __len__(self) -> int:
        return len(self._container)

    def __str__(self) -> str:
        return f"Queue({list(self._container)})"

def run_queue_demo():
    """Execution demo showcasing FIFO operations and performance."""
    print("--- Python Shorts: High-Performance Queue Service ---")
    
    # Initialize a queue with a capacity of 5
    my_queue = QueueService(capacity=5)
    
    # 1. Enqueue Operations
    print("[Action]: Enqueueing elements 10, 20, 30")
    my_queue.enqueue(10)
    my_queue.enqueue(20)
    my_queue.enqueue(30)
    print(f" -> Current State: {my_queue}")

    # 2. Peek Operation
    print(f"[Action]: Peek Front Element: {my_queue.peek()}")

    # 3. Dequeue Operations
    print(f"[Action]: Dequeueing: {my_queue.dequeue()}")
    print(f" -> Current State after Dequeue: {my_queue}")

    # 4. Capacity Handling
    print("[Action]: Filling queue to capacity (max=5)")
    my_queue.enqueue(40)
    my_queue.enqueue(50)
    my_queue.enqueue(60)
    print(f" -> Current State: {my_queue}")
    print(f"[Action]: Attempting overflow enqueue")
    my_queue.enqueue(70)

if __name__ == "__main__":
    run_queue_demo()
