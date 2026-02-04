"""
File: PerfectNumber.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    A computational utility for identifying perfect numbers. In number theory, 
    a perfect number is a positive integer that is equal to the sum of its 
    proper divisors (aliquot sum).

Mathematical Logic:
    A number n is perfect if sigma_1(n) = 2n, where sigma_1 is the 
    divisor function. This implementation uses an optimized O(sqrt(n)) 
    divisor summation algorithm.
"""

import math

class PerfectNumberVerifier:
    """Scholarly implementation of perfect number classification."""

    @staticmethod
    def is_perfect(n: int) -> bool:
        """
        Determines if an integer n is a perfect number.

        Args:
            n (int): The integer to verify.

        Returns:
            bool: True if n is perfect, False otherwise.
        """
        # Perfect numbers must be positive integers > 1
        if n < 2:
            return False

        # Optimized O(sqrt(n)) divisor sum
        # Starting with 1, as it is a proper divisor for all n > 1
        aliquot_sum = 1
        sqrt_n = int(math.sqrt(n))

        for i in range(2, sqrt_n + 1):
            if n % i == 0:
                aliquot_sum += i
                # If i^2 != n, add the paired divisor
                if i * i != n:
                    aliquot_sum += n // i

        return aliquot_sum == n

def run_perfect_demo():
    """Execution demo showcasing number classification."""
    print("--- Python Shorts: Perfect Number Verification Service ---")
    
    # Well-known perfect numbers
    perfect_vectors = [6, 28, 496, 8128]
    # Non-perfect numbers
    imperfect_vectors = [12, 100, 31, 8]

    print("[Testing Perfect Numbers]")
    for n in perfect_vectors:
        result = PerfectNumberVerifier.is_perfect(n)
        print(f" -> n = {n:4}: {'Perfect' if result else 'Not Perfect'}")

    print("\n[Testing Imperfect Numbers]")
    for n in imperfect_vectors:
        result = PerfectNumberVerifier.is_perfect(n)
        print(f" -> n = {n:4}: {'Perfect' if result else 'Not Perfect'}")

if __name__ == "__main__":
    run_perfect_demo()
