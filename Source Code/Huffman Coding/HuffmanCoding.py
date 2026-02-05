"""
File: HuffmanCoding.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    This module implements Huffman Coding, a popular algorithm for lossless 
    data compression. It uses a greedy approach to build a prefix-free binary 
    tree based on character frequencies, assigning shorter codes to more 
    frequent characters.

Complexity Analysis:
    - Time Complexity: O(n log n) where n is the number of unique characters.
    - Space Complexity: O(n) to store the Huffman tree and code mappings.

Logic:
    1. Calculate frequencies of all characters in the input string.
    2. Build a min-priority queue (min-heap) of leaf nodes for each character.
    3. While there is more than one node in the heap:
       a. Extract two nodes with minimum frequency.
       b. Create a new internal node with a frequency equal to the sum of the two nodes.
       c. Add the new node back to the heap.
    4. Traverse the tree from root to leaves to assign "0" for left and "1" for right children, forming the Huffman codes.
"""

import heapq
from collections import Counter
from typing import Dict, Optional


class HuffmanNode:
    """
    A node in the Huffman Tree.
    """
    def __init__(self, char: Optional[str], freq: int):
        self.char = char
        self.freq = freq
        self.left: Optional['HuffmanNode'] = None
        self.right: Optional['HuffmanNode'] = None

    def __lt__(self, other: 'HuffmanNode'):
        """Less than comparison for the priority queue (based on frequency)."""
        return self.freq < other.freq


class HuffmanCodingService:
    """
    A service class for data compression using Huffman Coding.
    """

    def __init__(self):
        self.codes: Dict[str, str] = {}
        self.reverse_mapping: Dict[str, str] = {}

    def _build_tree(self, text: str) -> Optional[HuffmanNode]:
        """Builds the Huffman tree from input text."""
        if not text:
            return None

        frequency = Counter(text)
        priority_queue = [HuffmanNode(char, freq) for char, freq in frequency.items()]
        heapq.heapify(priority_queue)

        while len(priority_queue) > 1:
            node_left = heapq.heappop(priority_queue)
            node_right = heapq.heappop(priority_queue)

            # Create internal node (char=None)
            merged = HuffmanNode(None, node_left.freq + node_right.freq)
            merged.left = node_left
            merged.right = node_right
            heapq.heappush(priority_queue, merged)

        return heapq.heappop(priority_queue)

    def _generate_codes(self, node: Optional[HuffmanNode], current_code: str):
        """Recursively generates Huffman codes."""
        if node is None:
            return

        if node.char is not None:
            self.codes[node.char] = current_code
            self.reverse_mapping[current_code] = node.char
            return

        self._generate_codes(node.left, current_code + "0")
        self._generate_codes(node.right, current_code + "1")

    def encode(self, text: str) -> str:
        """Encodes the input text."""
        if not text:
            return ""

        root = self._build_tree(text)
        self.codes = {}
        self.reverse_mapping = {}
        self._generate_codes(root, "")

        encoded_text = "".join(self.codes[char] for char in text)
        return encoded_text

    def decode(self, encoded_text: str) -> str:
        """Decodes the bitstream back to original text."""
        current_code = ""
        decoded_text = ""

        for bit in encoded_text:
            current_code += bit
            if current_code in self.reverse_mapping:
                decoded_text += self.reverse_mapping[current_code]
                current_code = ""

        return decoded_text


def main():
    """
    Demonstrates the scholarly Huffman Coding implementation.
    """
    print("--- Huffman Coding Service Demo ---")
    
    sample_text = "huffman coding is efficient"
    print(f"\nOriginal Text: '{sample_text}'")
    
    service = HuffmanCodingService()
    encoded = service.encode(sample_text)
    
    print("\nGenerated Huffman Codes:")
    for char in sorted(service.codes.keys()):
        print(f"  '{char}': {service.codes[char]}")
        
    print(f"\nEncoded Bitstream: {encoded}")
    print(f"Original Bits: {len(sample_text) * 8}")
    print(f"Encoded Bits: {len(encoded)}")
    print(f"Compression Ratio: {len(encoded) / (len(sample_text) * 8):.2f}")
    
    decoded = service.decode(encoded)
    print(f"\nDecoded Text: '{decoded}'")
    print(f"Integrity Check: {'Passed' if decoded == sample_text else 'Failed'}")
    
    print("\n--- Demo Complete ---")


if __name__ == "__main__":
    main()
