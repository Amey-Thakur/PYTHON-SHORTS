"""
File: PrimeNumber.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    A computational utility for primality verification. This module 
    implements an optimized trial division algorithm leveraging wheel 
    factorization (skipping multiples of 2 and 3) to achieve 
    high-performance verification.

Mathematical Logic:
    A prime number is a natural number greater than 1 that has no positive 
    divisors other than 1 and itself. Primality can be verified in 
    O(sqrt(n)) time. Further optimization (Wheel Factorization) exploits 
    the property that all primes greater than 3 are of the form 6k +/- 1.
"""

import math

class PrimalityEngine:
    """Scholarly implementation of primality verification services."""

    @staticmethod
    def is_prime(n: int) -> bool:
        """
        Determines if an integer n is a prime number.

        Args:
            n (int): The integer to verify.

        Returns:
            bool: True if n is prime, False otherwise.
        """
        # 1. Handling small integers and non-primes
        if n <= 1:
            return False
        if n <= 3:
            return True # 2 and 3 are prime

        # 2. Optimized Wheel Factorization (skipping even numbers and multiples of 3)
        if n % 2 == 0 or n % 3 == 0:
            return False

        # 3. Iterative trial division up to sqrt(n) using 6k +/- 1 rule
        # We start searching from 5 and increment by 6 in each step
        limit = int(math.sqrt(n))
        for i in range(5, limit + 1, 6):
            if n % i == 0 or n % (i + 2) == 0:
                return False
                
        return True

def run_primality_demo():
    """Execution demo showcasing optimized primality testing."""
    print("--- Python Shorts: Primality Verification Service ---")
    
    test_vectors = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # Primes
    composite_vectors = [4, 9, 15, 21, 25, 27, 33, 35, 49, 51] # Composites
    boundary_vectors = [-1, 0, 1] # Boundaries

    print("[Testing Prime Vectors]")
    for n in test_vectors:
        print(f" -> n = {n:2}: {'Prime' if PrimalityEngine.is_prime(n) else 'Composite'}")

    print("\n[Testing Composite Vectors]")
    for n in composite_vectors:
        print(f" -> n = {n:2}: {'Prime' if PrimalityEngine.is_prime(n) else 'Composite'}")

    print("\n[Testing Boundary Vectors]")
    for n in boundary_vectors:
        print(f" -> n = {n:2}: {'Prime' if PrimalityEngine.is_prime(n) else 'Composite'}")

if __name__ == "__main__":
    run_primality_demo()
