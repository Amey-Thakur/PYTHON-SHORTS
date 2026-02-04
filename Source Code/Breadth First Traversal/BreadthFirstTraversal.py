"""
File: BreadthFirstTraversal.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    Breadth-First Traversal (or Level-Order Traversal) of a binary tree 
    visits all nodes at the current level before moving to the next level.
    This implementation uses a FIFO queue for O(N) efficiency.

Complexity Analysis:
    - Time Complexity: O(N), where N is the number of nodes.
    - Space Complexity: O(W), where W is the maximum width of the tree 
      (queue size).

Logic:
    1. Initialize an empty list for results and a queue with the root node.
    2. While the queue is not empty:
       a. Dequeue the front node.
       b. Append its value to the result list.
       c. Enqueue its children (left then right) if they exist.
    3. Return the result list.
"""

from collections import deque
from typing import Optional, List, Any

class Node:
    """Represents a node in a binary tree."""
    def __init__(self, data: Any):
        self.data = data
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

def breadth_first_traversal(root: Optional[Node]) -> List[Any]:
    """
    Performs level-order traversal on a binary tree.

    Args:
        root (Optional[Node]): The root node of the binary tree.

    Returns:
        List[Any]: List of node values in BFS order.
    """
    if root is None:
        return []

    result = []
    queue = deque([root])

    while queue:
        current = queue.popleft()
        result.append(current.data)

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return result

def run_bfs_demo() -> None:
    """Demonstrates Breadth-First Traversal."""
    print("--- Python Shorts: Breadth-First Traversal Demo ---")
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    bfs_order = breadth_first_traversal(root)
    print(f"Level-Order Result: {bfs_order}")

if __name__ == '__main__':
    run_bfs_demo()
