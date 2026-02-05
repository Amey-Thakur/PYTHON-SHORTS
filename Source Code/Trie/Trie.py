"""
File: Trie.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    This module implements a Trie (Prefix Tree), a specialized set-based 
    data structure used to store a dynamic set of strings. It provides 
    efficient prefix-based searching, word insertion, and auto-complete 
    functionality.

Complexity Analysis:
    - Time Complexity: 
        - Insertion: O(L) where L is the length of the word.
        - Search: O(L).
        - Prefix Search: O(L).
    - Space Complexity: O(N * L * Σ) where N is number of words, L avg length, 
      and Σ is alphabet size.

Logic:
    1. Each node in the Trie represents a single character of a word.
    2. Words sharing common prefixes share the same path from the root.
    3. A boolean flag 'is_end_of_word' marks the terminal character of a path.
    4. Auto-complete: Traverse to the end of the prefix, then perform DFS 
       to find all reachable terminal nodes.
"""

from typing import Dict, List, Optional


class TrieNode:
    """
    A node in the Trie data structure.
    """
    def __init__(self):
        self.children: Dict[str, 'TrieNode'] = {}
        self.is_end_of_word: bool = False


class TrieService:
    """
    A service class providing Trie-based prefix tree operations.
    """

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the Trie.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        """
        Searches for a complete word in the Trie.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        """
        Returns True if any word in the Trie starts with the given prefix.
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def autocomplete(self, prefix: str) -> List[str]:
        """
        Returns a list of all words in the Trie that share the given prefix.
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        
        results: List[str] = []
        self._dfs(node, prefix, results)
        return results

    def _dfs(self, node: TrieNode, path: str, results: List[str]) -> None:
        """
        Depth-First Search to collect all words from a given node.
        """
        if node.is_end_of_word:
            results.append(path)
        
        for char, child_node in sorted(node.children.items()):
            self._dfs(child_node, path + char, results)


def main():
    """
    Demonstrates the Trie (Prefix Tree) implementation.
    """
    print("--- Trie (Prefix Tree) Service Demo ---")
    
    service = TrieService()
    dictionary = ["apple", "app", "application", "aptitude", "ball", "bat", "batch"]
    
    print(f"Feeding dictionary: {dictionary}")
    for word in dictionary:
        service.insert(word)
        
    print("\nSearch Operations:")
    print(f"  Search 'apple': {service.search('apple')}")
    print(f"  Search 'apply': {service.search('apply')}")
    print(f"  Search 'app': {service.search('app')}")
    
    print("\nPrefix Operations:")
    print(f"  Starts with 'app': {service.starts_with('app')}")
    print(f"  Starts with 'bat': {service.starts_with('bat')}")
    print(f"  Starts with 'cat': {service.starts_with('cat')}")
    
    print("\nAutocomplete Operations:")
    prefix = "app"
    suggestions = service.autocomplete(prefix)
    print(f"  Suggestions for '{prefix}': {suggestions}")
    
    prefix_b = "ba"
    suggestions_b = service.autocomplete(prefix_b)
    print(f"  Suggestions for '{prefix_b}': {suggestions_b}")
    
    print("\n--- Demo Complete ---")


if __name__ == "__main__":
    main()
