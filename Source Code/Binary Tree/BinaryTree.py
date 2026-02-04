"""
File: BinaryTree.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    A Binary Tree is a non-linear data structure where each node has at 
    most two children (left and right). This implementation provides 
    standard structure and recursive traversal methods (In-order, Pre-order, Post-order).

Complexity Analysis:
    - Traversal: O(N), where N is the number of nodes.
    - Height: O(N) in worst case (skewed tree).
    - Space Complexity: O(H) recursion stack where H is the height.

Logic:
    1. Define a `Node` class for data and pointers.
    2. Implement recursive algorithms for standard depth-first traversals.
    3. Include utility functions for tree size and max height.
"""

from typing import Optional, List, Any

class Node:
    """Represents a node in a binary tree."""
    def __init__(self, data: Any):
        self.data = data
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

class BinaryTree:
    """Standard Binary Tree implementation with DFS traversals."""
    def __init__(self, root_val: Optional[Any] = None):
        self.root = Node(root_val) if root_val is not None else None

    def preorder(self, node: Optional[Node], result: List[Any]) -> None:
        """Root -> Left -> Right"""
        if node:
            result.append(node.data)
            self.preorder(node.left, result)
            self.preorder(node.right, result)

    def inorder(self, node: Optional[Node], result: List[Any]) -> None:
        """Left -> Root -> Right"""
        if node:
            self.inorder(node.left, result)
            result.append(node.data)
            self.inorder(node.right, result)

    def postorder(self, node: Optional[Node], result: List[Any]) -> None:
        """Left -> Right -> Root"""
        if node:
            self.postorder(node.left, result)
            self.postorder(node.right, result)
            result.append(node.data)

    def get_height(self, node: Optional[Node]) -> int:
        """Calculates the maximum depth of the tree."""
        if node is None:
            return 0
        return 1 + max(self.get_height(node.left), self.get_height(node.right))

def run_binary_tree_demo() -> None:
    """Demonstrates binary tree creation and traversal."""
    print("--- Python Shorts: Binary Tree Structure Demo ---")
    bt = BinaryTree(1)
    bt.root.left = Node(2)
    bt.root.right = Node(3)
    bt.root.left.left = Node(4)
    bt.root.left.right = Node(5)

    res_in = []
    bt.inorder(bt.root, res_in)
    print(f"In-order Traversal: {res_in}")

    res_pre = []
    bt.preorder(bt.root, res_pre)
    print(f"Pre-order Traversal: {res_pre}")

    print(f"Tree Height: {bt.get_height(bt.root)}")

if __name__ == '__main__':
    run_binary_tree_demo()
