"""
File: SinglyLinkedList.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    This module implements a Singly Linked List (SLL), a fundamental linear data 
    structure consisting of a sequence of elements where each element points to 
    the next. It demonstrates dynamic memory allocation, pointer-based traversal, 
    and basic ADT operations including insertion, deletion, and searching.

Complexity Analysis:
    - Time Complexity:
        - Insertion (Head): O(1)
        - Deletion: O(n)
        - Search: O(n)
        - Access: O(n)
    - Space Complexity: O(n) total, O(1) auxiliary per operation.

Logic:
    1. Define a Node class encapsulating data and a pointer to the next node.
    2. Maintain a head pointer to the first element of the list.
    3. Insertion (Head): Create a new node, point its next to the current head, 
       and update the head pointer.
    4. Deletion: Traverse to find the target, then bypass the node by linking 
       the predecessor's next pointer to the successor.
    5. Traversal: Sequential visit of each node from head until null (None).
"""

from typing import Any, List, Optional


class Node:
    """
    Represents a constituent element within the singly linked list.
    """
    def __init__(self, data: Any, next_node: Optional['Node'] = None):
        self.data = data
        self.next = next_node


class SinglyLinkedListService:
    """
    A service class providing Discrete Abstract Data Type (ADT) operations
     for a Singly Linked List implementation.
    """

    def __init__(self):
        self.head: Optional[Node] = None
        self._size: int = 0

    def is_empty(self) -> bool:
        """Checks if the collection contains no elements."""
        return self.head is None

    def add(self, data: Any) -> None:
        """
        Inserts a new element at the head of the list.
        
        Args:
            data: The payload to be stored in the new node.
        """
        new_node = Node(data, self.head)
        self.head = new_node
        self._size += 1

    def remove(self, target: Any) -> bool:
        """
        Removes the first occurrence of the specified element.
        
        Args:
            target: The value to identify for removal.
            
        Returns:
            True if the element was removed, False otherwise.
        """
        current = self.head
        previous = None
        found = False

        while current is not None:
            if current.data == target:
                found = True
                break
            previous = current
            current = current.next

        if found:
            if previous is None:
                self.head = current.next  # Target was head
            else:
                previous.next = current.next
            self._size -= 1
            return True
        return False

    def search(self, item: Any) -> bool:
        """
        Performs a sequential search for the specified item.
        
        Args:
            item: The value to search for.
            
        Returns:
            Boolean indicating presence of the item.
        """
        current = self.head
        while current is not None:
            if current.data == item:
                return True
            current = current.next
        return False

    def get_all_data(self) -> List[Any]:
        """
        Retrieves all elements in the list as a sequential collection.
        """
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

    def size(self) -> int:
        """Returns the total cardinality of the set of nodes."""
        return self._size


def main():
    """
    Demonstrates the scholarly Singly Linked List implementation.
    """
    print("--- Singly Linked List Service Demo ---")
    
    sll = SinglyLinkedListService()
    
    print(f"Is list empty? {sll.is_empty()}")
    
    # Populating list
    data_points = [42, 32, 22, 2, 12]
    print(f"Populating list with: {data_points}")
    for val in data_points:
        sll.add(val)
        
    print(f"Current Size: {sll.size()}")
    print(f"Sequence: {sll.get_all_data()}")
    
    # Search demonstrations
    target_1 = 12
    target_2 = 93
    print(f"Searching for {target_1}: {sll.search(target_1)}")
    print(f"Searching for {target_2}: {sll.search(target_2)}")
    
    # Removal demonstration
    print(f"Removing {target_1}...")
    sll.remove(target_1)
    print(f"Sequence after removal: {sll.get_all_data()}")
    print(f"Final Size: {sll.size()}")


if __name__ == "__main__":
    main()
