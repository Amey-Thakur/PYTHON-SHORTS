"""
File: RedBlackTree.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    This module implements a Red-Black Tree, a type of self-balancing binary 
    search tree. It ensures that the tree remains approximately balanced, 
    guaranteeing logarithmic time complexity for basic operations.

Complexity Analysis:
    - Search: O(log n)
    - Insertion: O(log n)
    - Deletion: O(log n)
    - Space: O(n)

Rules of Red-Black Trees:
    1. Every node is either red or black.
    2. The root is black.
    3. Every leaf (NIL) is black.
    4. If a node is red, then both its children are black.
    5. For each node, all simple paths from the node to descendant leaves 
       contain the same number of black nodes.
"""

from typing import Optional, List


class Node:
    """A node in the Red-Black Tree."""
    def __init__(self, data: int, color: str = "red"):
        self.data = data
        self.color = color  # "red" or "black"
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None
        self.parent: Optional[Node] = None


class RedBlackTreeService:
    """
    Service class for Red-Black Tree operations.
    """

    def __init__(self):
        self.nil = Node(0, color="black")
        self.root = self.nil

    def insert(self, key: int):
        """Inserts a new key and performs balancing."""
        new_node = Node(key)
        new_node.left = self.nil
        new_node.right = self.nil
        
        parent = None
        current = self.root

        while current != self.nil:
            parent = current
            if new_node.data < current.data:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.data < parent.data:
            parent.left = new_node
        else:
            parent.right = new_node

        if new_node.parent is None:
            new_node.color = "black"
            return

        if new_node.parent.parent is None:
            return

        self._fix_insert(new_node)

    def _fix_insert(self, k: Node):
        """Maintains Red-Black properties after insertion."""
        while k.parent.color == "red":
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == "red":
                    u.color = "black"
                    k.parent.color = "black"
                    k.parent.parent.color = "red"
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self._right_rotate(k)
                    k.parent.color = "black"
                    k.parent.parent.color = "red"
                    self._left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right
                if u.color == "red":
                    u.color = "black"
                    k.parent.color = "black"
                    k.parent.parent.color = "red"
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self._left_rotate(k)
                    k.parent.color = "black"
                    k.parent.parent.color = "red"
                    self._right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = "black"

    def _left_rotate(self, x: Node):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _right_rotate(self, x: Node):
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def inorder_traversal(self, node: Node, result: List[str]):
        """Collects nodes in-order with color information."""
        if node != self.nil:
            self.inorder_traversal(node.left, result)
            result.append(f"{node.data}({node.color})")
            self.inorder_traversal(node.right, result)

    def search(self, key: int) -> bool:
        """Searches for a key in the tree."""
        current = self.root
        while current != self.nil:
            if key == current.data:
                return True
            if key < current.data:
                current = current.left
            else:
                current = current.right
        return False


def main():
    """Demonstrates Red-Black Tree insertion and balancing."""
    print("--- Red-Black Tree Service Demo ---")
    
    rbt = RedBlackTreeService()
    keys = [10, 20, 30, 15, 25, 5, 1]
    
    print(f"Inserting keys: {keys}")
    for k in keys:
        rbt.insert(k)
        
    res = []
    rbt.inorder_traversal(rbt.root, res)
    print("\nIn-order Traversal (Key and Color):")
    print(" -> ".join(res))
    
    print("\nSearch Tests:")
    for test_key in [15, 100, 1]:
        found = rbt.search(test_key)
        print(f"  Key {test_key}: {'Found' if found else 'Not Found'}")
        
    print("\nObservation: The tree maintains BST property and balance through rotations/recoloring.")
    print("--- Demo Complete ---")


if __name__ == "__main__":
    main()
