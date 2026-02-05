"""
File: PrimeSieve.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    This module implements the Sieve of Eratosthenes, an ancient and efficient 
    algorithm for finding all prime numbers up to a specified limit. It uses 
    an iterative marking process to eliminate composite numbers.

Complexity Analysis:
    - Time Complexity: O(n log log n) where n is the upper limit.
    - Space Complexity: O(n) to store the boolean marking array.

Logic:
    1. Create a boolean array "is_prime" of size n+1, initialized to True.
    2. Set is_prime[0] and is_prime[1] to False.
    3. Iterate from p = 2 to the square root of n.
    4. If is_prime[p] is True, it is a prime:
       Mark all multiples of p (p*p, p*p + p, ...) as False.
    5. All indices that remain True in the array are prime numbers.
"""

import math
from typing import List


class PrimeSieveService:
    """
    A service class for generating prime numbers using the Sieve of Eratosthenes.
    """

    def __init__(self, limit: int):
        self.limit = limit

    def get_primes(self) -> List[int]:
        """
        Executes the sieve algorithm and returns a list of primes.
        """
        if self.limit < 2:
            return []

        is_prime = [True] * (self.limit + 1)
        is_prime[0] = is_prime[1] = False

        for p in range(2, int(math.sqrt(self.limit)) + 1):
            if is_prime[p]:
                # Mark multiples starting from p*p
                for i in range(p * p, self.limit + 1, p):
                    is_prime[i] = False

        return [p for p, prime in enumerate(is_prime) if prime]


def main():
    """
    Demonstrates the Prime Sieve (Sieve of Eratosthenes) implementation.
    """
    print("--- Prime Sieve (Sieve of Eratosthenes) Service Demo ---")
    
    limit = 100
    service = PrimeSieveService(limit)
    primes = service.get_primes()
    
    print(f"\nFinding primes up to {limit}:")
    print(f"Total Primes Found: {len(primes)}")
    print("\nPrimes:")
    # Print in chunks of 10 for readability
    for i in range(0, len(primes), 10):
        print(", ".join(map(str, primes[i:i+10])))
        
    print("\n--- Higher Range Test ---")
    large_limit = 1000
    service_large = PrimeSieveService(large_limit)
    primes_large = service_large.get_primes()
    print(f"Total Primes up to {large_limit}: {len(primes_large)}")
    print(f"Last 5 Primes: {primes_large[-5:]}")
    
    print("\n--- Demo Complete ---")


if __name__ == "__main__":
    main()
