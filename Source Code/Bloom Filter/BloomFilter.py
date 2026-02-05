"""
File: BloomFilter.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    This module implements a Bloom Filter, a space-efficient probabilistic 
    data structure used to test whether an element is a member of a set. 
    It demonstrates the tradeoff between space and the probability of 
    false positives.

Complexity Analysis:
    - Time Complexity: 
        - Insertion: O(k) where k is the number of hash functions.
        - Lookup: O(k).
    - Space Complexity: O(m) where m is the size of the bit array.

Logic:
    1. Initialize a bit array of size 'm' with all zeros.
    2. Use 'k' independent hash functions.
    3. Insertion: For an item, compute 'k' hashes and set bits at those 
       indices to 1.
    4. Lookup: Compute 'k' hashes. If all corresponding bits are 1, the 
       item *might* be in the set. If any bit is 0, the item is *definitely* 
       not in the set.
    5. False Positives: Bloom filters never have false negatives, but 
       may return false positives due to hash collisions.
"""

import hashlib
import math
from typing import List


class BloomFilterService:
    """
    A service class for probabilistic set membership testing via Bloom Filter.
    """

    def __init__(self, expected_items: int, false_positive_rate: float):
        """
        Initializes the Bloom Filter with optimal bit-array size and hash count.
        """
        self.m = self._get_size(expected_items, false_positive_rate)
        self.k = self._get_hash_count(self.m, expected_items)
        self.bit_array = [0] * self.m

    def _get_size(self, n: int, p: float) -> int:
        """Returns the optimal size of the bit array (m)."""
        m = -(n * math.log(p)) / (math.log(2) ** 2)
        return int(m)

    def _get_hash_count(self, m: int, n: int) -> int:
        """Returns the optimal number of hash functions (k)."""
        k = (m / n) * math.log(2)
        return int(k)

    def _hashes(self, item: str) -> List[int]:
        """
        Generates 'k' hash values for a given item using 
        different salts with SHA-256.
        """
        hashes = []
        for i in range(self.k):
            # Use i as a salt to generate k independent hashes
            combined = f"{i}{item}".encode('utf-8')
            digest = hashlib.sha256(combined).hexdigest()
            # Map the digest to an index in the bit array
            index = int(digest, 16) % self.m
            hashes.append(index)
        return hashes

    def add(self, item: str) -> None:
        """Adds an item to the Bloom Filter."""
        for index in self._hashes(item):
            self.bit_array[index] = 1

    def contains(self, item: str) -> bool:
        """
        Checks if an item is likely in the set.
        Returns False if definitely not present, True if likely present.
        """
        for index in self._hashes(item):
            if self.bit_array[index] == 0:
                return False
        return True


def main():
    """
    Demonstrates the Bloom Filter functionality.
    """
    print("--- Bloom Filter Service Demo ---")
    
    n = 20  # Expected items
    p = 0.05  # 5% False Positive Rate
    
    service = BloomFilterService(n, p)
    print(f"Parameters: n={n}, p={p}")
    print(f"Optimal Size (m): {service.m} bits")
    print(f"Optimal Hashes (k): {service.k}")
    
    # Items to add
    fruits = ["apple", "banana", "cherry", "date", "elderberry"]
    print(f"\nAdding items: {fruits}")
    for fruit in fruits:
        service.add(fruit)
        
    # Testing membership
    test_items = ["apple", "banana", "grape", "kiwi", "cherry"]
    print("\nMembership Tests:")
    for item in test_items:
        result = service.contains(item)
        status = "Maybe Present" if result else "Definitely Not Present"
        print(f"  '{item}': {status}")
        
    print("\nObservation: 'grape' and 'kiwi' are definitely not present.")
    print("--- Demo Complete ---")


if __name__ == "__main__":
    main()
