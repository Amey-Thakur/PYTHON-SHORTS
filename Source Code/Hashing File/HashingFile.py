"""
File: HashingFile.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    A cryptographic utility for calculating the hash sum of files. This module 
    implements a stream-based hashing mechanism using the Merkle–Damgård 
    construction, enabling efficient integrity verification of large 
    datasets with minimal memory overhead.

Mathematical Logic:
    A cryptographic hash function H maps arbitrary-sized data to a fixed-size 
    bit string. This implementation ensures determinism and collision resistance 
    by processing file contents in discrete blocks (B-byte chunks).
"""

import hashlib
import os
from typing import Optional

class FileHasher:
    """Scholarly implementation of a stream-based cryptographic file hashing service."""
    
    def __init__(self, block_size: int = 65536):
        self.block_size = block_size

    def calculate_hash(self, file_path: str, algorithm: str = 'sha256') -> str:
        """
        Computes the digest of a file using a streaming buffer.

        Args:
            file_path (str): Absolute or relative path to the target file.
            algorithm (str): The hash algorithm to employ (e.g., 'sha256', 'md5').

        Returns:
            str: The hexadecimal representation of the digest.

        Raises:
            FileNotFoundError: If the specified file does not exist.
            ValueError: If the requested algorithm is not supported.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File system error: Resource not found at {file_path}")

        try:
            hasher = hashlib.new(algorithm)
        except ValueError:
            raise ValueError(f"Cryptographic error: Algorithm '{algorithm}' is unsupported.")

        with open(file_path, 'rb') as f:
            while True:
                buffer = f.read(self.block_size)
                if not buffer:
                    break
                hasher.update(buffer)
        
        return hasher.hexdigest()

def run_hashing_demo():
    """Execution demo for verifying file integrity via cryptographic digests."""
    print("--- Python Shorts: Cryptographic Hash Functions & Integrity ---")
    
    # Create a temporary verification artifact
    temp_file = "integrity_test.txt"
    with open(temp_file, "w") as f:
        f.write("Python Shorts: Scholarly Hashing Demonstration.")

    hasher = FileHasher()
    
    try:
        print(f"\n[Target]: {temp_file}")
        sha256_sum = hasher.calculate_hash(temp_file, 'sha256')
        print(f"[SHA-256]: {sha256_sum}")
        
        md5_sum = hasher.calculate_hash(temp_file, 'md5')
        print(f"[MD5]: {md5_sum}")
        
    except Exception as e:
        print(f"[Error]: {e}")
    finally:
        if os.path.exists(temp_file):
            os.remove(temp_file)

if __name__ == "__main__":
    run_hashing_demo()
