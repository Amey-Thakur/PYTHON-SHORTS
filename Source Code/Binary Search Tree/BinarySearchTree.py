"""
File: BinarySearchTree.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    A Binary Search Tree (BST) is a node-based binary tree data structure 
    where the left subtree of a node contains only nodes with keys lesser 
    than the node’s key, and the right subtree contains only nodes with 
    keys greater. This implementation provides standard insertion, search, 
    and deletion operations.

Complexity Analysis:
    - Search/Insert/Delete: Average O(log N), Worst O(N) if the tree is skewed.
    - Space Complexity: O(N) for storing N nodes.

Logic:
    1. Define a `Node` class to represent each element in the tree.
    2. Use recursion for clean tree traversal and modification.
    3. Ensure BST property is maintained during all mutation operations.
    4. Implement in-order traversal for verification of sorted order.
"""

from typing import Optional, List, Any

class BSTNode:
    """Represents a single node in the Binary Search Tree."""
    def __init__(self, key: Any):
        self.key = key
        self.left: Optional[BSTNode] = None
        self.right: Optional[BSTNode] = None

class BinarySearchTree:
    """A standard Binary Search Tree implementation."""
    def __init__(self):
        self.root: Optional[BSTNode] = None

    def insert(self, key: Any) -> None:
        """Inserts a new key into the BST."""
        if self.root is None:
            self.root = BSTNode(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node: BSTNode, key: Any) -> None:
        if key < node.key:
            if node.left is None:
                node.left = BSTNode(key)
            else:
                self._insert_recursive(node.left, key)
        else:
            if node.right is None:
                node.right = BSTNode(key)
            else:
                self._insert_recursive(node.right, key)

    def search(self, key: Any) -> bool:
        """Searches for a key in the BST."""
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node: Optional[BSTNode], key: Any) -> bool:
        if node is None:
            return False
        if node.key == key:
            return True
        if key < node.key:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)

    def delete(self, key: Any) -> None:
        """Deletes a key from the BST."""
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, node: Optional[BSTNode], key: Any) -> Optional[BSTNode]:
        if node is None:
            return None

        if key < node.key:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.key:
            node.right = self._delete_recursive(node.right, key)
        else:
            # Node with only one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Node with two children: Get the inorder successor
            temp = self._min_value_node(node.right)
            node.key = temp.key
            node.right = self._delete_recursive(node.right, temp.key)

        return node

    def _min_value_node(self, node: BSTNode) -> BSTNode:
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder_traversal(self) -> List[Any]:
        """Returns the in-order traversal of the tree (sorted)."""
        results: List[Any] = []
        self._inorder_recursive(self.root, results)
        return results

    def _inorder_recursive(self, node: Optional[BSTNode], results: List[Any]) -> None:
        if node:
            self._inorder_recursive(node.left, results)
            results.append(node.key)
            self._inorder_recursive(node.right, results)

def run_bst_demo() -> None:
    """Demonstrates basic BST operations."""
    print("--- Python Shorts: Binary Search Tree Demo ---")
    bst = BinarySearchTree()
    keys = [50, 30, 20, 40, 70, 60, 80]
    
    for k in keys:
        bst.insert(k)
        
    print(f"In-order Traversal (Sorted): {bst.inorder_traversal()}")
    print(f"Search for 40: {'Found' if bst.search(40) else 'Not Found'}")
    
    print("Deleting 20...")
    bst.delete(20)
    print(f"In-order Traversal: {bst.inorder_traversal()}")

if __name__ == '__main__':
    run_bst_demo()
