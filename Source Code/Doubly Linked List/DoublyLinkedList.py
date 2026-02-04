"""
File: DoublyLinkedList.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    A high-fidelity implementation of a Doubly Linked List (DLL), a bidirectional 
    linear data structure. This module provides efficient O(1) head/tail 
    operations and robust pointer management to ensure architectural integrity.

Mathematical Foundation:
    A Doubly Linked List can be modeled as a Directed Acyclic Graph (DAG) G = (V, E) 
    where each vertex v ∈ V has at most two edges (prev, next). 
    The sequence is defined by the total ordering of nodes from head to tail.
"""

from typing import Optional, Any, List

class Node:
    """Represents a discrete node within a bidirectional data structure."""
    def __init__(self, data: Any):
        self.data = data
        self.next: Optional['Node'] = None
        self.prev: Optional['Node'] = None

class DoublyLinkedList:
    """Academic implementation of a Doubly Linked List with Head and Tail pointers."""
    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self._count = 0

    def append(self, data: Any) -> None:
        """Adds an element to the terminal end of the list. Complexity: O(1)."""
        new_node = Node(data)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self._count += 1

    def prepend(self, data: Any) -> None:
        """Adds an element to the initial end of the list. Complexity: O(1)."""
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self._count += 1

    def delete(self, data: Any) -> bool:
        """Deletes the first occurrence of data. Complexity: O(N)."""
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                
                self._count -= 1
                return True
            current = current.next
        return False

    def reverse(self) -> None:
        """Reverses the list in-place by swapping next and prev pointers. Complexity: O(N)."""
        current = self.head
        self.tail = self.head
        while current:
            # Swap pointers
            current.next, current.prev = current.prev, current.next
            # Update head
            if current.prev is None:
                self.head = current
            # Move to the "old" next (which is now prev)
            current = current.prev

    def to_list(self) -> List[Any]:
        """Serializes the list structure into a standard Python list."""
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def __len__(self) -> int:
        return self._count

def run_dll_demo():
    """Execution demo following user-specified validation scenarios."""
    print("--- Python Shorts: Bidirectional Data Structures (Doubly Linked List) ---")
    
    # TC-01: Initialization
    dll = DoublyLinkedList()
    print(f"[TC-01] Initialized: List={dll.to_list()} | Size={len(dll)}")
    
    # TC-02: Append
    dll.append(10)
    dll.append(20)
    print(f"[TC-02] Append(10, 20): {dll.to_list()}")
    
    # TC-03: Prepend
    dll.prepend(5)
    print(f"[TC-03] Prepend(5): {dll.to_list()}")
    
    # TC-04: Reversal
    dll.reverse()
    print(f"[TC-04] Reversed: {dll.to_list()}")
    
    # TC-05: Removal
    # Resetting for specific TC-05 data state [5, 10, 20] -> Delete 10 -> [5, 20]
    dll.reverse() # Back to [5, 10, 20]
    print(f"[TC-05] State before delete(10): {dll.to_list()}")
    dll.delete(10)
    print(f"[TC-05] State after delete(10): {dll.to_list()}")

if __name__ == "__main__":
    run_dll_demo()
