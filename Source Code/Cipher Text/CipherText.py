"""
File: CipherText.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    A scholarly implementation of the Caesar Cipher, a classic substitution 
    cryptosystem. It utilizes modular arithmetic over the additive group 
    Z_26 for character transformations while maintaining case and formatting.

Mathematical Foundation:
    E_k(x) = (x + k) mod 26
    D_k(y) = (y - k) mod 26
    Where k is the secret key (shift).
"""

def caesar_cipher(text: str, shift: int, decrypt: bool = False) -> str:
    """
    Transforms text using Caesar's additive cipher logic.
    
    Args:
        text (str): The plaintext or ciphertext to transform.
        shift (int): The cryptographic key representing the alphabet shift.
        decrypt (bool): Boolean flag to toggle inverse transformation.

    Returns:
        str: The resultant transformed string.
    """
    # Inverse shift for decryption: k' = -k mod 26
    if decrypt:
        shift = -shift
        
    result = []
    for char in text:
        if char.isalpha():
            # Standardize to 0-25 range by subtracting ASCII base
            # 'A' = 65, 'a' = 97
            base = ord('A') if char.isupper() else ord('a')
            # Modular addition: f(x) = (x + k) mod 26
            transformed_char = chr(base + (ord(char) - base + shift) % 26)
            result.append(transformed_char)
        else:
            # Preserve non-alphabetical characters (identity mapping)
            result.append(char)
            
    return "".join(result)

def run_demo():
    """Demonstrates encryption and decryption cycles."""
    print("--- Python Shorts: Cryptography - Caesar Cipher ---")
    
    scenarios = [
        {"msg": "Hello World!", "key": 3},
        {"msg": "Cryptography in Z_26", "key": 13}, # ROT13 equivalent
        {"msg": "Amey & Mega 2022", "key": 5}
    ]
    
    for s in scenarios:
        encrypted = caesar_cipher(s["msg"], s["key"])
        decrypted = caesar_cipher(encrypted, s["key"], decrypt=True)
        print(f"\n[Key: {s['key']}]")
        print(f"Original : {s['msg']}")
        print(f"Cipher   : {encrypted}")
        print(f"Verified : {decrypted}")

if __name__ == "__main__":
    run_demo()
