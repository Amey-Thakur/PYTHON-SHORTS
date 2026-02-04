"""
File: Password_Generator.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    A cryptographically secure utility for generating high-entropy passwords. 
    This module leverages the 'secrets' module, which provides access to the 
    most secure source of randomness available on the operating system.

Mathematical Logic:
    The security of a password is characterized by its Information Entropy (H), 
    calculated as:
    H = log2(L^k) = k * log2(L)
    where L is the size of the character pool and k is the password length. 
    This generator maximizes H by utilizing a uniform distribution across 
    extended character sets.
"""

import secrets
import string
from typing import Optional

class SecurePasswordGenerator:
    """Scholarly implementation of cryptographic random string generation."""

    # Extended character pool for maximum entry
    DEFAULT_POOL = string.ascii_letters + string.digits + string.punctuation

    @staticmethod
    def generate(length: int = 16, pool: Optional[str] = None) -> str:
        """
        Generates a secure password using CSPRNG.

        Args:
            length (int): The desired character count.
            pool (Optional[str]): Custom character set pool.

        Returns:
            str: The generated high-entropy password.
        """
        character_set = pool if pool is not None else SecurePasswordGenerator.DEFAULT_POOL
        
        # secrets.choice is cryptographically secure (CSPRNG)
        password = "".join(secrets.choice(character_set) for _ in range(length))
        return password

def run_security_demo():
    """Execution demo showcasing entropy and secure generation."""
    print("--- Python Shorts: Secure Password Generation Service ---")
    
    generator = SecurePasswordGenerator()
    
    # 1. Standard Secure Password (16 chars)
    print(f"[Input]: Requesting default 16-character secure string")
    pw1 = generator.generate(16)
    print(f" -> Result: {pw1}\n")

    # 2. Extended Entropy Password (32 chars)
    print(f"[Input]: Requesting high-entropy 32-character secure string")
    pw2 = generator.generate(32)
    print(f" -> Result: {pw2}\n")

    # 3. Alphanumeric Only (12 chars)
    print(f"[Input]: Requesting 12-character alphanumeric string")
    alpha_pool = string.ascii_letters + string.digits
    pw3 = generator.generate(12, alpha_pool)
    print(f" -> Result: {pw3}")

if __name__ == "__main__":
    run_security_demo()