"""
File: LCM.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    An efficient implementation for calculating the Least Common Multiple (LCM). 
    This module utilizes the fundamental relationship between GCD and LCM, 
    leveraging the Euclidean Algorithm to achieve O(log(min(a, b))) complexity.

Mathematical Logic:
    For any two integers a and b, the LCM is defined as the smallest positive 
    integer that is divisible by both. The calculation is optimized via the 
    identity: LCM(a, b) = |a * b| / GCD(a, b).
"""

class arithmetic_service:
    """Number Theory utility service for fundamental arithmetic operations."""
    
    @staticmethod
    def calculate_gcd(a: int, b: int) -> int:
        """Computes the Greatest Common Divisor using the Euclidean Algorithm."""
        while b:
            a, b = b, a % b
        return abs(a)

    @staticmethod
    def calculate_lcm(a: int, b: int) -> int:
        """
        Computes the Least Common Multiple using the GCD identity.

        Args:
            a (int): First integer.
            b (int): Second integer.

        Returns:
            int: The Least Common Multiple of a and b.
        """
        if a == 0 or b == 0:
            return 0
        
        # LCM(a, b) = |a * b| / GCD(a, b)
        # Using integer division to avoid float precision issues
        gcd = arithmetic_service.calculate_gcd(a, b)
        return abs(a * b) // gcd

def run_lcm_demo():
    """Execution demo with diverse numerical test vectors."""
    print("--- Python Shorts: Least Common Multiple (LCM) ---")
    
    test_vectors = [
        (12, 18),
        (5, 7),
        (15, 20),
        (24, 60),
        (0, 10),
        (1, 100)
    ]

    for a, b in test_vectors:
        lcm_val = arithmetic_service.calculate_lcm(a, b)
        print(f"[Input]: (a={a}, b={b})")
        print(f" -> Result: LCM = {lcm_val}\n")

if __name__ == "__main__":
    run_lcm_demo()
