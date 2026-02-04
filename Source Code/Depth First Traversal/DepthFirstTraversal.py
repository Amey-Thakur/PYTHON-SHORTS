"""
File: DepthFirstTraversal.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    A scholarly implementation of Depth-First Traversal (DFS) for tree structures. 
    This module provides algorithms for exploring nodes in a deterministic order 
    by descending deep into branches before backtracking.

Mathematical Logic:
    Depth-First Search (DFS) is a strategy for traversing a graph or tree. 
    For a tree rooted at node R, DFS visits all nodes in the subtrees 
    rooted at children of R before visiting R itself (Post-order) or 
    between sibling visits.
"""

from typing import Optional, List, Any

class Node:
    """Represents a discrete node within a binary tree structure."""
    def __init__(self, data: Any):
        self.data = data
        self.left: Optional['Node'] = None
        self.right: Optional['Node'] = None

class DFSTraversal:
    """Scholarly implementation of Depth-First Traversal algorithms."""
    
    @staticmethod
    def pre_order(node: Optional[Node]) -> List[Any]:
        """
        Visits the current node first, then left subtree, then right subtree.
        Order: Root -> Left -> Right
        """
        if node is None:
            return []
        res = [node.data]
        res.extend(DFSTraversal.pre_order(node.left))
        res.extend(DFSTraversal.pre_order(node.right))
        return res

    @staticmethod
    def in_order(node: Optional[Node]) -> List[Any]:
        """
        Visits the left subtree, then the current node, then right subtree.
        Order: Left -> Root -> Right
        """
        if node is None:
            return []
        res = DFSTraversal.in_order(node.left)
        res.append(node.data)
        res.extend(DFSTraversal.in_order(node.right))
        return res

    @staticmethod
    def post_order(node: Optional[Node]) -> List[Any]:
        """
        Visits left subtree, then right subtree, then the current node.
        Order: Left -> Right -> Root
        """
        if node is None:
            return []
        res = DFSTraversal.post_order(node.left)
        res.extend(DFSTraversal.post_order(node.right))
        res.append(node.data)
        return res

    @staticmethod
    def iterative_pre_order(root: Optional[Node]) -> List[Any]:
        """
        Iterative implementation of Pre-order traversal using an explicit LIFO stack.
        """
        if root is None:
            return []
        result = []
        stack = [root]
        while stack:
            curr = stack.pop()
            result.append(curr.data)
            # Push right child first so left is processed first
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
        return result

def run_dfs_demo():
    """Execution demo with a standardized binary tree topology."""
    print("--- Python Shorts: Algorithmic Depth-First Traversal ---")
    
    # Constructing a standard binary tree:
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print(f"Pre-order  (Root-L-R): {DFSTraversal.pre_order(root)}")
    print(f"In-order   (L-Root-R): {DFSTraversal.in_order(root)}")
    print(f"Post-order (L-R-Root): {DFSTraversal.post_order(root)}")
    print(f"Iterative Pre-order  : {DFSTraversal.iterative_pre_order(root)}")

if __name__ == "__main__":
    run_dfs_demo()
