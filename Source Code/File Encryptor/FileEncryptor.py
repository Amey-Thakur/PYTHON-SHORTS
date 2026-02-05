"""
File: FileEncryptor.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    This module implements a file encryption and decryption service using 
    the XOR cipher algorithm. It demonstrates symmetric-key cryptography 
    by transforming file buffers using bitwise operations.

Complexity Analysis:
    - Time Complexity: O(N) where N is the number of bytes in the file.
    - Space Complexity: O(1) as it processes data in chunks.

Logic:
    1. Key-Stream Generation: Repeat the secret key to match file length.
    2. Encryption: Result = Byte XOR Key_Byte.
    3. Decryption: Because (A XOR B) XOR B = A, the same logic decrypts.
    4. Practicality: While simple, it illustrates the foundation of 
       stream ciphers like RC4.
"""

import os
from typing import Optional


class FileEncryptorService:
    """
    A service class for symmetric-key file encryption using XOR logic.
    """

    def __init__(self, key: str):
        if not key:
            raise ValueError("Encryption key cannot be empty.")
        self.key = key.encode('utf-8')

    def process_file(self, input_path: str, output_path: str):
        """
        Encrypts or decrypts a file (symmetric) and saves the result.
        Processes in chunks to handle large files efficiently.
        """
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"Source file not found: {input_path}")

        key_length = len(self.key)
        chunk_size = 65536  # 64KB chunks

        with open(input_path, 'rb') as f_in, open(output_path, 'wb') as f_out:
            i = 0
            while True:
                chunk = f_in.read(chunk_size)
                if not chunk:
                    break
                
                processed_chunk = bytearray()
                for byte in chunk:
                    # Bitwise XOR with the corresponding key byte
                    processed_chunk.append(byte ^ self.key[i % key_length])
                    i += 1
                
                f_out.write(processed_chunk)


def main():
    """
    Demonstrates the File Encryptor service.
    """
    print("--- File Encryptor Service Demo ---")
    
    secret_key = "Amey_And_Mega_Super_Secret_Key"
    encryptor = FileEncryptorService(secret_key)
    
    # Create a sample text file
    sample_file = "sample.txt"
    encrypted_file = "encrypted.dat"
    decrypted_file = "decrypted.txt"
    
    content = "Securing algorithmic research: Amey and Mega protect Python Shorts using bitwise XOR ciphers."
    print(f"\nOriginal Message: '{content}'")
    
    with open(sample_file, "w") as f:
        f.write(content)
        
    print(f"Encrypting '{sample_file}' to '{encrypted_file}'...")
    encryptor.process_file(sample_file, encrypted_file)
    
    with open(encrypted_file, "rb") as f:
        print(f"Encrypted Content (Hex): {f.read().hex()[:50]}...")
        
    print(f"Decrypting '{encrypted_file}' back to '{decrypted_file}'...")
    encryptor.process_file(encrypted_file, decrypted_file)
    
    with open(decrypted_file, "r") as f:
        restored_content = f.read()
        print(f"Restored Message: '{restored_content}'")
        print(f"Integrity Check: {'Passed' if restored_content == content else 'Failed'}")
    
    # Cleanup demo files (optional, keeping for Output log)
    print("\n--- Demo Complete ---")


if __name__ == "__main__":
    main()
